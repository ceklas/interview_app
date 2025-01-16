from pathlib import Path
import os,sys
import environ

# .env dosyasını oku
env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = env.bool('DEBUG', default=True)

# SECRET_KEY'i .env dosyasından al
SECRET_KEY = env.str('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'interview_app',
    'app',  
    'rest_framework',
    'drf_yasg',
]

# PostgreSQL veritabanı ayarları
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://127.0.0.1:5432/interview_app_db')
}

# Eğer test çalıştırılıyorsa SQLite bellek içi veritabanı kullan
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Bellek içi veritabanı
    }

    # Testlerde önbellek kullanımı
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # Bellek içi önbellek
            'LOCATION': 'unique-snowflake',
        }
    }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Statik dosyalar için gerekli ayarlar
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Statik dosyalarınızın bulunduğu dizin
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # Üretim ortamında statik dosyaların toplanacağı dizin

# ROOT_URLCONF ayarını ekleyin
ROOT_URLCONF = 'interview_app.urls'