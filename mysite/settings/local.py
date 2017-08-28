from .base import *  # noqa

INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = '127.0.0.1'

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# LOCAL EMAIL SETTINGS
EMAIL_PORT = 1025
EMAIL_HOST = 'localhost'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddaac',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
