import os
import json
import psycopg2
from psycopg2 import Error # Импорт исключений для обработки ошибок

# Функция для установления соединения с базой данных
def connect_postgres(host, user, password, dbname):
    try:
        conn = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                dbname=dbname)
        return conn
    except (Exception, Error) as error:
        print("Ошибка при подключении к PostgreSQL:", error)
        raise

# Функция для выполнения SQL-запросов
def execute_query(conn, query, params=None):
    try:
        # Открытие курсора для выполнения запросов
        cursor = conn.cursor()
        # Выполнение запроса с параметрами
        cursor.execute(query, params)
        # Фиксирование
        conn.commit()
        # Закрытие
        cursor.close()
    except (Exception, Error) as error:
        print(f"Ошибка при выполнении запроса '{query}': {error}")
        raise


if __name__ == "__main__":
    host = "app_db"
    # Получем данные из переменной окруженеия 
    user = os.environ.get("POSTGRES_USER")
    password = os.environ.get("POSTGRES_PASSWORD")
    dbname = os.environ.get("POSTGRES_DB")

    try:
        conn = connect_postgres(host, user, password, dbname)
        
        create_schema = "CREATE SCHEMA IF NOT EXISTS demo_db;"
        execute_query(conn, create_schema)
        create_table = """CREATE TABLE IF NOT EXISTS demo_db.test_table (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(50) CHECK (LENGTH(name) BETWEEN 4 AND 11),
                            surname VARCHAR(255),
                            state VARCHAR(255),
                            age INT CHECK (age > 0)
                          );
                       """
        execute_query(conn, create_table)
        # Чтение данных из именованного тома docker 
        with open('/app/data/values.json') as f:
            data = json.load(f)
        for item in data:
            # Преобразование элемента в кортеж
            values = tuple(item)
            insert_query = """INSERT INTO demo_db.test_table (name, surname, state, age)
                              VALUES (%s, %s, %s, %s);
                           """
            execute_query(conn, insert_query, values)
        cursor = conn.cursor()
       
        count_query = "SELECT COUNT(*) FROM demo_db.test_table;" 
        # Выполняем запрос
        cursor.execute(count_query)
        # Извлечение результата
        result = cursor.fetchone()[0]
        print(f'Всего записей в таблице: {result}')

        select_where = '''SELECT MIN(age), MAX(age) 
                        FROM demo_db.test_table 
                        WHERE LENGTH(name) <6;'''
        cursor.execute(select_where)
        print('Максимальный и минимальный возраст для имен, длина которых меньше 6 символов')
        print(cursor.fetchone())
        

        cursor.close()


    # Закрываем соединение 
    finally:
        if conn:
            conn.close()
            print("Соединение закрыто")

            