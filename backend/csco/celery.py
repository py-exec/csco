import os
from celery import Celery

# تنظیمات اولیه
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csco.settings')

app = Celery('csco')

# لود تنظیمات `Celery` از فایل تنظیمات جنگو
app.config_from_object('django.conf:settings', namespace='CELERY')

# جستجو برای `tasks.py` در هر اپلیکیشن جنگو
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')