"""
Django settings for rmdsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# ===== path configuration =====
# setting direcotry
ETC_DIR = os.path.dirname(os.path.dirname(__file__))
# project directory
PROJECT_DIR = os.path.dirname(ETC_DIR)
# template directory
TEMPLATE_DIR = os.path.join(PROJECT_DIR, 'templates')
# mdeia directory
MEDIA_DIR = os.path.join(PROJECT_DIR, 'media')
# static directory, collectstatic to this directory
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')
STATIC_ROOT_DIR = os.path.join(PROJECT_DIR, '..', 'static')
# ===== end path configuration =====

# ===== DEBUG CONFIGURATION =====
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
# ===== END DEBUG CONFIGURATION =====

# ====== MANAGER CONFIGURATION ======
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
# ADMINS = (
#     ('Your Name', 'your_email@example.com'),
# )
# # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
# MANAGERS = ADMINS
# ====== END MANAGER CONFIGURATION =======


# ====== DATABASE CONFIGURATION =======
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ETC_DIR, 'db.sqlite3'),
    }
}
# ====== END DATABASE CONFIGURATION =======

# ====== GENERAL CONFIGURATION =======
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# ====== END GENERAL CONFIGURATION =======

# ====== MEDIA CONFIGURATION ======
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = MEDIA_DIR
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# ====== END MEDIA CONFIGURATION ======

# ====== STATIC FILE CONFIGURATION ======
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = STATIC_ROOT_DIR
STATICFILES_DIRS = (
    STATIC_DIR,
)
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# ====== END STATIC FILE CONFIGURATION ======


# ====== SECRET CONFIGURATION ======
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tk0xi)gvk30uezsn2z#f9qr_4#rc16!66rx*en%&iva&%d+$39'
# ====== END SECRET CONFIGURATION ======


# ====== SITE CONFIGURATION ======
ALLOWED_HOSTS = []
# ====== END SITE CONFIGURATION ======

# ======  TEMPLATE CONFIGURATION ======
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    TEMPLATE_DIR,
)
# ======  END TEMPLATE CONFIGURATION ======


# ====== MIDDLEWARE CONFIGURATION ======
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# ====== END MIDDLEWARE CONFIGURATION ======

# ====== URL CONFIGURATION ======
ROOT_URLCONF = 'etc.urls'
# ====== END URL CONFIGURATION ======


# ====== APP CONFIGURATION ======
BUILTIN_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    ''
)

THIRD_PARTY_APPS = (
    # 'crispy_forms'
    # 'debug_toolbar',
    # 'django_extensions'
)

INSTALLED_APPS = BUILTIN_APPS + THIRD_PARTY_APPS

# ====== END APP CONFIGURATION ======


# ====== LOGGING CONFIGURATION ======
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# ====== END LOGGING CONFIGURATION ======


# ====== WSGI CONFIGURATION ======
WSGI_APPLICATION = 'etc.wsgi.application'
# ====== END WSGI CONFIGURATION ======
