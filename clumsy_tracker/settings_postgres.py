from .settings import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'clumsy_db'),
        'USER': os.environ.get('POSTGRES_USER', 'clumsy_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'clumsy_pass'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
