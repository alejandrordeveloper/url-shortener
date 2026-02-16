from django.shortcuts import render, redirect
from .forms import URLForm
from .models import ShortenedURL
import random
import string

def generate_short_code(length=6):
	characters = string.ascii_letters + string.digits
	return ''.join(random.choices(characters, k=length))

def shorten_url(request):
	if request.method == 'POST':
		form = URLForm(request.POST)
		if form.is_valid():
			original_url = form.cleaned_data['original_url']
			# Generar un código corto único (sin prefijo)
			short_code = generate_short_code()
			while ShortenedURL.objects.filter(short_code=short_code).exists():
				short_code = generate_short_code()
			# Guardar en la base de datos
			shortened = ShortenedURL.objects.create(
				original_url=original_url,
				short_code=short_code
			)
			# Pasar el dominio al template para mostrar el link completo
			full_short_url = request.build_absolute_uri(f'/{short_code}')
			return render(request, 'shortener/result.html', {'shortened': shortened, 'full_short_url': full_short_url})
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
