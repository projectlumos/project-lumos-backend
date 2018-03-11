import dj_database_url
# secret key
SECRET_KEY_DEFAULT = '93pye=z=**bajl6ie5euzul*gzz8b8+*)ku&1b=b)dkv%+o-q5'
SECRET_KEY = '93pye=z=**bajl6ie5euzul*gzz8b8+*)ku&1b=b)dkv%+o-q5'

# database
DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
DATABASE_NAME = 'pl_dev'
DATABASE_USER = ''
DATABASE_PASSWORD = ''

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


SENDGRID_API_KEY='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'