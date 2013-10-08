from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1','sistema.linussio.net','sync.malignani.local']

BROKER_URL = 'amqp://guest:guest@localhost:5672/'
CELERY_RESULT_BACKEND = "amqp"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gestione_scuola',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'mosa',
        'PASSWORD': 'sambackett',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


