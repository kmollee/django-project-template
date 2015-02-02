"""Development settings and globals."""
from __future__ import absolute_import
from os.path import join, normpath
import os
from .base import *
import logging

logger = logging.getLogger(__name__)

# env detect
ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True

# openshift
if ON_OPENSHIFT:
    MEDIA_ROOT = normpath(
        join(os.environ['OPENSHIFT_DATA_DIR'], 'media'))


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
        if ON_OPENSHIFT:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': os.environ['OPENSHIFT_APP_NAME'],
                    'USER': os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
                    'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
                    'HOST': os.environ['OPENSHIFT_MYSQL_DB_HOST'],
                    'PORT': os.environ['OPENSHIFT_MYSQL_DB_PORT']
                }
            }
        else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': '',
                    'USER': '',
                    'PASSWORD': '',
                }
            }
else:
    # SQLITE3
    if ON_OPENSHIFT:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'database', 'db.sqlite3'),
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': join(ETC_DIR, 'data.db'),
            }
        }
# ====== END DATABASE CONFIGURATION ======

SECRET_KEY = ''

ALLOWED_HOSTS = ['']
