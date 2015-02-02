"""Development settings and globals."""
from __future__ import absolute_import
from os.path import join
from .base import *
import logging

logger = logging.getLogger(__name__)

# ====== DEBUG CONFIGURATION ======
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
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
                'NAME': 'rmd',
                'USER': 'rmdadmin',
                'PASSWORD': 'zR48VyuRxjvv6QZa',
            }
        }
else:
    # SQLITE3
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

SECRET_KEY = ''

ALLOWED_HOSTS = ['']
