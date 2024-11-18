FROM python:3.12-slim

WORKDIR /app

# Копируем скрипт подключения к базе данных
COPY connect_db.py /app/
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/app/connect_db.py"]