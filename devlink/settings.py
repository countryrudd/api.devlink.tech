from pathlib import Path

import dj_database_url
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
CORS_ORIGIN_WHITELIST = config('CORS_ORIGIN_WHITELIST', cast=Csv())
REQUESTS_TIMEOUT = int(config('REQUESTS_TIMEOUT'))
GITHUB_API_KEY = config('GITHUB_API_KEY')

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'rest_framework',
    'corsheaders',
    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
]

ROOT_URLCONF = 'devlink.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'devlink.wsgi.application'

DATABASES = {'default': dj_database_url.parse(config('DATABASE_URL'))}

AUTH_USER_MODEL = 'api.User'
AUTH0_API_IDENTIFIER = config('AUTH0_API_IDENTIFIER')
AUTH0_DOMAIN = config('AUTH0_DOMAIN')

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
]

REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_METADATA_CLASS': None,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_PAYLOAD_GET_USERNAME_HANDLER':
        'devlink.auth.utils.jwt_get_username_from_payload_handler',
    'JWT_DECODE_HANDLER':
        'devlink.auth.utils.jwt_decode_token',
    'JWT_ALGORITHM': 'RS256',
    'JWT_AUDIENCE': AUTH0_API_IDENTIFIER,
    'JWT_ISSUER': AUTH0_DOMAIN,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
