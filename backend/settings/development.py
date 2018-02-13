from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DATABASE_NAME', 'default_db'),
        'USER': get_env_variable('DATABASE_USER', 'username'),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD', 'password'),
        'HOST': '',
        'PORT': '',
    }
}
