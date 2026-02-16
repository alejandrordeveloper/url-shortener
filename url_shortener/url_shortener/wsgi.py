"""
WSGI project for url_shortener.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys

# Agrega la carpeta url_shortener al sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'url_shortener.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
