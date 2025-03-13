# استفاده از Python 3.13
FROM python:3.13

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن `requirements.txt` از `backend/`
COPY ../backend/requirements.txt .

# نصب پکیج‌های مورد نیاز
RUN pip install --upgrade --no-cache-dir --requirement requirements.txt --retries 5 --timeout 100

# کپی کردن کل پروژه بعد از نصب پکیج‌ها (برای کش بهتر)
COPY ../backend .

# ایجاد دایرکتوری‌های استاتیک و مدیا
RUN mkdir -p /frontend/static /frontend/staticfiles /frontend/media

# تنظیم متغیرهای محیطی برای static
ENV STATIC_ROOT=/frontend/staticfiles
ENV STATICFILES_DIRS=/frontend/static

# اجرای collectstatic
RUN python manage.py collectstatic --noinput

# مشخص کردن پورت
EXPOSE 8000

# اجرای سرور با Gunicorn
CMD ["gunicorn", "csco.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2", "--timeout", "120"]