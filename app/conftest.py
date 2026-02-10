import django
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_backend.settings')

def pytest_configure():
    if not settings.configured:
        django.setup()
