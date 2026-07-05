import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
import os

# For Render
ALLOWED_HOSTS = ['medicare-lnan.onrender.com', 'localhost', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://medicare-lnan.onrender.com']

# Static files for admin CSS
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECRET_KEY = 'django-insecure-change-this-in-production'

# Turn this False once everything works
DEBUG = os.environ.get('DEBUG', 'False')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pharmacy',  # your app
]

# ... rest of your file stays the same
