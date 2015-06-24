# -*- coding: utf-8 -*-
# Refer to https://docs.djangoproject.com/en/dev/ref/settings/ for docs

from __future__ import unicode_literals

import os

from . import rel, get_env_setting

from .common.logs import *
from .common.compress import *
from .common.thumbnails import *
from .common.multilingual import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = "UTC"
LANGUAGE_CODE = "fr"
SITE_ID = 1

APPEND_SLASH = False

LANGUAGES = [
    ('en', 'English'),
    ('fr', 'Français'),
]

USE_I18N = True
USE_L10N = True
USE_TZ = True

SECRET_KEY = "thisisasbvcxecretkey"


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
    #"django.template.loaders.eggs.Loader",
]

TEMPLATE_DIRS = [
    rel("templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",

    'sekizai.context_processors.sekizai',
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",

    "content.middleware.multilingual.EnforcedMultilingualURLMiddleware",
]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "compressor",
    "sekizai",
    "easy_thumbnails",
    "image_cropping",
    "leaflet",
    "parsley",
    "sortedm2m",
    'm2m_history',
    'taggit',
    "mptt",
    "apetizer",
    "content",
    'content.todo',
    "planrecup",
]

WSGI_APPLICATION = "wsgi.application"

#SESSION_ENGINE = "website.sessions.cached_db"
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTH_USER_MODEL = "auth.User"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

ALLOWED_HOSTS = ['*']

BASICAUTH_USERNAME = 'website'
BASICAUTH_PASSWORD = 'website'

BASICAUTH_WHITELIST = ['/']

ROOT_URLCONF = "planrecup.urls"

MEDIA_ROOT = 'medias'
STATIC_ROOT = 'static'

STATIC_URL = '/static/'
MEDIA_URL = '/medias/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db'
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    },
    "locmem": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    },
    "dummy": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

CACHES['items'] = {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    'LOCATION': 'content',
    'TIMEOUT': 900,
    'OPTIONS': {
        'MAX_ENTRIES': 10000
    },
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


