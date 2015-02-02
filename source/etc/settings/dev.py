"""Development settings and globals."""
from __future__ import absolute_import
from os.path import join
from .base import *


# ====== DEBUG CONFIGURATION ======
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# ====== END DEBUG CONFIGURATION ======


# ====== EMAIL CONFIGURATION ======
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ====== END EMAIL CONFIGURATION ======


# ====== DATABASE CONFIGURATION ======
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES_TYPE = 'MYSQL'

if DATABASES_TYPE == 'MYSQL':
    try:
        import pymysql
    except ImportError as e:
        logger.error('can not import pymysql, need to install this module')
    else:
        pymysql.install_as_MySQLdb()
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': '',
                'USER': '',
                'PASSWORD': '',
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': join(ETC_DIR, 'data.db'),
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
# ====== END DATABASE CONFIGURATION ======


# ====== TOOLBAR CONFIGURATION ======
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
DEBUG_TOOLBAR_PATCH_SETTINGS = True
# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
# ======END TOOLBAR CONFIGURATION ======
