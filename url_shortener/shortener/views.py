from django.shortcuts import render
from .forms import URLForm
from .models import ShortenedURL
import random
import string
from django.core import signing
from django.db.utils import OperationalError
import logging

logger = logging.getLogger(__name__)
TOKEN_SALT = 'shortener.stateless'

def generate_short_code(length=6):
	characters = string.ascii_letters + string.digits
	return ''.join(random.choices(characters, k=length))

def shorten_url(request):
	if request.method == 'POST':
		form = URLForm(request.POST)
		if form.is_valid():
			original_url = form.cleaned_data['original_url']
			try:
				# Generar un código corto único (sin prefijo)
				short_code = generate_short_code()
				while ShortenedURL.objects.filter(short_code=short_code).exists():
					short_code = generate_short_code()

				# En local/hosting con DB writable: persistimos normalmente.
				shortened = ShortenedURL.objects.create(
					original_url=original_url,
					short_code=short_code
				)
				full_short_url = request.build_absolute_uri(f'/{short_code}')
				return render(request, 'shortener/result.html', {
					'shortened': shortened,
					'full_short_url': full_short_url,
					'redirect_target': original_url,
					'is_stateless': False,
				})
			except OperationalError:
				# En Vercel (filesystem read-only), usamos token firmado sin DB.
				token = signing.dumps({'u': original_url}, salt=TOKEN_SALT, compress=True)
				full_short_url = request.build_absolute_uri(f'/go/{token}/')
				logger.warning('Database is not writable. Falling back to stateless short URLs.')
				return render(request, 'shortener/result.html', {
					'shortened': None,
					'full_short_url': full_short_url,
					'redirect_target': original_url,
					'is_stateless': True,
				})
	else:
		form = URLForm()
	return render(request, 'shortener/form.html', {'form': form})


# Vista para redireccionar el short_code
from django.http import HttpResponseRedirect, Http404
def shorten_url_redirect(request, short_code):
	try:
		url_obj = ShortenedURL.objects.get(short_code=short_code)
		return HttpResponseRedirect(url_obj.original_url)
	except ShortenedURL.DoesNotExist:
		raise Http404('Shortened URL not found')


def shorten_url_redirect_token(request, token):
	try:
		payload = signing.loads(token, salt=TOKEN_SALT, max_age=60 * 60 * 24 * 30)
		return HttpResponseRedirect(payload['u'])
	except Exception:
		raise Http404('Shortened URL not found')
