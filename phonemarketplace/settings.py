from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-553xo&)es(l_8rxfzm=94j%z5*)f=1+^h(5-_i!$s0r3*+bgq+'

# Email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your-system-email@gmail.com'
EMAIL_HOST_PASSWORD = 'hbkb fkln bstx dcrf'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'marketplace',
    'seller',
    'customAdmin',
    'tailwind',
    'theme',
    'storages',
]

# Static files settings
STATIC_URL = 'static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # Example app-specific static dir
    os.path.join(BASE_DIR, "theme/static"),  # Another example
]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# WHITENOISE_USE_FINDERS = True
# WHITENOISE_ROOT = os.path.join(BASE_DIR, 'media')

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # Keep this one
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Ensure WhiteNoise is here
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/media' 

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']



DEBUG = os.getenv("DEBUG", "true") == "True"

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

ROOT_URLCONF = 'phonemarketplace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'phonemarketplace.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication settings
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'marketplace.backends.EmailAuthBackend',  # Custom backend
]

AUTH_USER_MODEL = 'marketplace.CustomUser'

LOGIN_URL = '/seller/'
LOGOUT_REDIRECT_URL = '/'

# Static files configuration (already configured above)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Ensure npm path is correct for Tailwind CSS (if using Tailwind)
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"





