import os

import dotenv
import pymysql

dotenv.load_dotenv()

TABLE_NAME = 'usuarios'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_ROOT_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)

with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            F'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL , '
            'PRIMARY KEY (id)'
            ') '
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # Limpa a tabela
        connection.commit()
        print(cursor)
    with connection.cursor() as cursor:
        cursor.execute(
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) VALUES ('Luiz', 24)"
        )
        connection.commit()
