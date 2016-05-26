from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_URL = "http://localhost:8000"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'