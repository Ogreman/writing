from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SITE_URL = "http://www.wizzarding.com"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'wizzarding.site@gmail.com'
EMAIL_HOST_PASSWORD = '06123Wizzard'
