import os
from pathlib import Path
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "../env/.env"
load_dotenv(ENV_PATH)

# امنیت و تنظیمات اصلی
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret-key")
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").replace('"', '').split(",")

# اپلیکیشن‌ها
INSTALLED_APPS = [
    # 'jet',  # 🔹 اضافه کردن django-jet
    'jazzmin',  # قالب مدیریت جنگو
    # 'jet.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',  # مدیریت استاتیک‌ها در حالت DEBUG=False
    'django_celery_beat',  # زمان‌بندی تسک‌های Celery
    'django_celery_results',  # ذخیره نتایج Celery
    'rest_framework',  # Django REST Framework
    'corsheaders',  # مدیریت CORS

]

# میان‌افزارها
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # مدیریت استاتیک‌ها
    'corsheaders.middleware.CorsMiddleware',  # فعال‌سازی CORS
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# فعال‌سازی CORS برای ارتباط با کلاینت‌های خارجی
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'csco.urls'
WSGI_APPLICATION = 'csco.wsgi.application'

# تنظیمات قالب‌ها
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["/frontend"],  # ✅ مسیر صحیح قالب‌ها
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# تنظیمات پایگاه داده (PostgreSQL)
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

# تنظیمات استاتیک و مدیا
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    Path("/frontend/static"),  # ✅ مسیر استاتیک در سطح root کانتینر
]
STATIC_ROOT = Path("/frontend/staticfiles")  # ✅ مسیر جمع‌آوری فایل‌های استاتیک
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = Path("/frontend/media")  # ✅ مسیر فایل‌های رسانه‌ای

# پیدا کردن فایل‌های استاتیک
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# کشینگ و سشن‌ها
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://csco_redis:6379/1"),
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# تنظیمات Celery و Redis
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://csco_redis:6379/1")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://csco_redis:6379/1")
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# Celery Beat زمان‌بندی تسک‌ها
# CELERY_BEAT_SCHEDULE = {
#     'example_task': {
#         'task': 'myapp.tasks.example_task',
#         'schedule': 30.0,  # هر 30 ثانیه اجرا شود
#     },
# }

# اعتبارسنجی رمز عبور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# تنظیمات زبان و منطقه زمانی
LANGUAGE_CODE = 'fa'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# تنظیمات ایمیل
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.example.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "your-email@example.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "your-email-password")

# کلید پیش‌فرض مدل‌ها
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
