from .base import *

ALLOWED_HOSTS = [
    'https://example.com',
]

ALLOWED_HOSTS = [
    'haadijafari.ir',
    'hadijafari.info',
    '127.0.0.1',
    'localhost',
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

MIDDLEWARE += [
    'csp.middleware.CSPMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ['SQL_NAME'],
#         'USER': os.environ['SQL_USER'],
#         'PASSWORD': os.environ['SQL_PASS'],
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'OPTIONS': {
#             'sql_mode': 'traditional',
#         }
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# reCaptcha
RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY_V2']
RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY_V2']
# RECAPTCHA_DOMAIN = 'www.recaptcha.net'
RECAPTCHA_REQUIRED_SCORE = 0.75

# STATIC_ROOT = '/home/[USER]/public_html/static'
# MEDIA_ROOT = '/home/[USER]/public_html/media'
STATIC_ROOT = BASE_DIR / "static_cdn"
MEDIA_ROOT = BASE_DIR / "media_cdn"
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "media",
    BASE_DIR / "frontend/vite-react/public",
    BASE_DIR / "frontend/vite-react/dist",
]
