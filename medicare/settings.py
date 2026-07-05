import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # ADD THIS LINE
import os

# For Render
ALLOWED_HOSTS = ['medicare-lnan.onrender.com', 'localhost', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://medicare-lnan.onrender.com']
