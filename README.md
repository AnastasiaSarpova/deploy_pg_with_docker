# Развертывание PostgreSQL с использованием Docker Compose
## Цель проекта

Проект предназначен для быстрого создания и настройки среды разработки с PostgreSQL, предоставляя удобный интерфейс для управления данными через Adminer. Это идеальный выбор для тестирования и обучения работе с базами данных.

Прокет позволяет развернуть БД Postgres и добавить в нее таблицу со сгенерированным списком людей:
name | surname | state | age  
|---|---|---|---|
Elizabeth|White|Nevada|33


![Снимок экрана от 2024-11-18 14-11-01](https://github.com/user-attachments/assets/94e319bd-570c-419f-9633-f054636fbdc1)

## Используемые технологии

- PostgreSQL
- Docker Compose
- Python (для генерации тестовых данных и вставки в бд)
- Adminer (веб-интерфейс для управления базами данных)

- ## Установка и запуск

1. Клонируйте репозиторий:
   
   $ git clone https://github.com/AnastasiaSarpova/deploy_pg_with_docker.git
   

2. Перейдите в директорию проекта:
   
   $ cd project_name
   

3. Запустите контейнеры с помощью Docker Compose с необходимой переменной POSTGRES_PASSWORD:
   
   $ POSTGRES_PASSWORD="ваш пароль" POSTGRES_DB = demo_db docker-compose up --build -d  
   VALUES_SIZE - необязательная переменная, для изменения размера сгенерированной таблицы, значение по умолчанию — 50

4. Доступ к веб-интерфейсу Adminer по адресу: http://localhost:8080. Используйте следующие учетные данные для подключения:
   - Движок	: PostgreSQL
   - Сервер: db
   - Имя пользователя: postgres
   - Пароль: "ваш пароль"

