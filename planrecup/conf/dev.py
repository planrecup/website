#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

THUMBNAIL_DEBUG = True

SECRET_KEY = "thisisasecretkey"

DOMAIN_NAME = "dev.planrecup.com"
SITE_NAME = "planrecup (dev)"

DEFAULT_FROM_EMAIL = "{} <hey@{}>".format(SITE_NAME, DOMAIN_NAME)
SERVER_EMAIL = "server@{}".format(DOMAIN_NAME)
EMAIL_SUBJECT_PREFIX = "[{} (dev)]".format(SITE_NAME)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db'
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"