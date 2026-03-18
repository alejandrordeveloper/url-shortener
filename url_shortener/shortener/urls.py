from .forms import URLForm
from .views import shorten_url, shorten_url_redirect, shorten_url_redirect_token
from django.urls import path

urlpatterns = [
	path('', shorten_url, name='shorten_url'),
	path('go/<str:token>/', shorten_url_redirect_token, name='shorten_url_redirect_token'),
	path('<str:short_code>/', shorten_url_redirect, name='shorten_url_redirect'),
]