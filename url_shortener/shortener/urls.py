from .forms import URLForm
from .views import shorten_url, shorten_url_redirect
from django.urls import path

urlpatterns = [
	path('', shorten_url, name='shorten_url'),
	path('<str:short_code>/', shorten_url_redirect, name='shorten_url_redirect'),
]