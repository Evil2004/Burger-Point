from .base import *
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

ADMIN_ENABLED = True
DEBUG = True

# database config

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')),
}


