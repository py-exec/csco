import os
from pathlib import Path
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# خواندن SECRET_KEY از .env
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret-key")

# تعیین مقدار DEBUG از .env (اگر مقدار در .env نبود، False در نظر گرفته شود)
DEBUG = os.getenv("DEBUG", "False") == "True"

# تعیین ALLOWED_HOSTS از .env (به صورت لیست)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'csco.urls'

import os
from pathlib import Path
from dotenv import load_dotenv

# مسیر `.env` را به صورت مطلق مشخص کن
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "../env/.env"

# بارگذاری متغیرهای محیطی
load_dotenv(ENV_PATH)  # این خط را اضافه کن تا Django مطمئن شود که .env خوانده شده است

# SECRET_KEY از .env خوانده می‌شود
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret-key")

# مقدار DEBUG از .env خوانده می‌شود
DEBUG = os.getenv("DEBUG", "False") == "True"

# لیست هاست‌های مجاز
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# تنظیمات پایگاه داده
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB", "csco_db"),
        'USER': os.getenv("POSTGRES_USER", "user"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD", "password"),
        'HOST': os.getenv("POSTGRES_HOST", "db"),
        'PORT': os.getenv("POSTGRES_PORT", "5432"),
    }
}


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

WSGI_APPLICATION = 'csco.wsgi.application'


# تنظیمات پایگاه داده (PostgreSQL از .env خوانده می‌شود)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB", "csco_db"),
        'USER': os.getenv("POSTGRES_USER", "user"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD", "password"),
        'HOST': os.getenv("POSTGRES_HOST", "db"),
        'PORT': os.getenv("POSTGRES_PORT", "5432"),
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

# تنظیمات زبان و منطقه زمانی
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# تنظیمات استاتیک فایل‌ها
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# پیش‌فرض برای مدل‌های دیتابیس
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'