import dj_database_url
#secret key
SECRET_KEY_DEFAULT = '93pye=z=**bajl6ie5euzul*gzz8b8+*)ku&1b=b)dkv%+o-q5'
#database
DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
DATABASE_NAME = 'default_db'
DATABASE_USER = 'username'
DATABASE_PASSWORD = 'password'

DATABASE_DEFAULT = dj_database_url.config(default='postgres://paritosh:Parwad321@localhost/backend2_db')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
