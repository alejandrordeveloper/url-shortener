import os
import sys
from pathlib import Path

# Add the Django project root (folder containing manage.py) to sys.path.
PROJECT_ROOT = Path(__file__).resolve().parent.parent / "url_shortener"
sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "url_shortener.settings")

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
