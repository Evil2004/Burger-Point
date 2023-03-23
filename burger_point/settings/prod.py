from .base import *
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

ADMIN_ENABLED = False


DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# cloudinary config

cloudinary.config (
    cloud_name=os.environ.get('CLOUDINARY_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')