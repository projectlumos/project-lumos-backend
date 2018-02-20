import dj_database_url
#secret key
SECRET_KEY_DEFAULT = '93pye=z=**bajl6ie5euzul*gzz8b8+*)ku&1b=b)dkv%+o-q5'

# don't keep any username and password for db in local env (sub with '' and store them as env vars in Heroku

#database
DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
DATABASE_NAME = 'default_db'
DATABASE_USER = 'username'
DATABASE_PASSWORD = 'password'

# what/why is this?
DATABASE_DEFAULT = dj_database_url.config(default='postgres://paritosh:Parwad321@localhost/backend2_db')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
