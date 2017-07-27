from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'GR_db',
        'USER': 'GR_admin',
        'PASSWORD': '76090',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}