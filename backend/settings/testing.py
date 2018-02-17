from .base import *
from .env_vars import DATABASE_ENGINE, DATABASE_USER, DATABASE_NAME, DATABASE_PASSWORD
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': get_env_variable('DATABASE_NAME', DATABASE_NAME),
        'USER': get_env_variable('DATABASE_USER', DATABASE_USER),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD', DATABASE_PASSWORD),
        'HOST': '',
        'PORT': '',
    }
}

import dj_database_url
DATABASES[‘default’] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = (‘HTTP_X_FORWARDED_PROTO’, ‘https’)
