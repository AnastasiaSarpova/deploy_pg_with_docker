FROM python:3.12-slim

WORKDIR /app

# Копируем скрипт генерации данных
COPY script_generate.py /app/

# Команда запуска скрипта
CMD ["python", "/app/script_generate.py"]
