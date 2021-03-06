import os
from backend.settings.base import *
from backend.settings.env_vars import DATABASE_ENGINE, DATABASE_USER, DATABASE_NAME, DATABASE_PASSWORD, \
    SECURE_PROXY_SSL_HEADER

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True
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

SENDGRID_API_KEY = get_env_variable('SENDGRID_API_KEY')


env = os.environ.copy()
db_url = env.get('DATABASE_URL', False)
if db_url != False:
    # to handle Heroku and local settings, DATABASE_URL present in env then run the following code
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()
    SECURE_PROXY_SSL_HEADER = SECURE_PROXY_SSL_HEADER

###########################################################################
# TODO SETTINGS ARE SUPER CONFUSING | FIX THEM
###########################################################################

# encryption string
'''
from cryptography.fernet import Fernet
Fernet.generate_key().decode('utf-8')
'''
LUMOS_ENCRYPTION_SEED = "UKkx3sfyCFjyiy1xpryXd6FGkgeQ_gMSJ2cU3_edx1o="
