# project-lumos-backend

## Prerequisites
If you haven't already, install and configure PostgreSQL on your local machine[(guide)](http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django "guide")

create a database table named 'default_db', username being 'username' and password bieng 'password' to use for development.

## Setup
Create a virtual environment in which to install Python pip packages. Use python3

Install development dependencies,

`pip install -r requirements.txt`

---

Setup database tables,

`python manage.py makemigrations`

`python manage.py migrate`

---

Run the web application locally,

`python manage.py runserver --settings=backend.settings.development` # 127.0.0.1:8000(localhost)


you can also set the environment variable in the virtual environment, to avoid writing the settings part everytime

`export DJANGO_SETTINGS_MODULE=backend.settings.development`
