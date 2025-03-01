FROM python:3.13

WORKDIR /app

# کپی کردن `requirements.txt` از `backend/`
COPY ../backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن بقیه پروژه
COPY ../backend .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]