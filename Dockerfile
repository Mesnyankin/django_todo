# Используем Python-образ
FROM python:3.12

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Запускаем сервер
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
RUN python manage.py collectstatic --noinput