import os
from pathlib import Path
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "../env/.env"
load_dotenv(ENV_PATH)

# امنیت و تنظیمات اصلی
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret-key") # SECRET_KEY از .env خوانده می‌شود
DEBUG = os.getenv("DEBUG", "False") == "True" # مقدار DEBUG از .env خوانده می‌شود
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").replace('"', '').split(",") # لیست هاست‌های مجاز

ROOT_URLCONF = 'csco.urls'
# مسیر `.env` را به صورت مطلق مشخص کن
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "../env/.env"

# بارگذاری متغیرهای محیطی
load_dotenv(ENV_PATH)  # این خط را اضافه کن تا Django مطمئن شود که .env خوانده شده است

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
        'USER': os.getenv("POSTGRES_USER", "py_exec"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD", "secure-password"),
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
LANGUAGE_CODE = 'fa'  # فارسی
TIME_ZONE = 'Asia/Tehran'  # منطقه زمانی ایران
USE_I18N = True
USE_TZ = True

# پیش‌فرض برای مدل‌های دیتابیس
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# تنظیمات Celery و Redis
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis_cache:6379/1")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://redis_cache:6379/1")

# تنظیمات ایمیل
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.example.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "your-email@example.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "your-email-password")

# تنظیمات سرویس پیامک (IPPANEL)
IPPANEL_API_KEY = os.getenv("IPPANEL_API_KEY", "your-ippanel-api-key")

# مسیرهای استاتیک و مدیا
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'backend/static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'backend/media'