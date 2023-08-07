import os

import dotenv
import pymysql   # type: ignore

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
    with connection.cursor() as cursor:
        sql = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) VALUES (%(nome)s, %(idade)s)"
        )

        data = {
            "nome": "João",
            "idade": 24,
        }

        cursor.execute(sql, data)
        connection.commit()
    with connection.cursor() as cursor:
        sql = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) VALUES (%(nome)s, %(idade)s)"
        )

        data2 = (
            {"nome": "Maria", "idade": 30},
            {"nome": "Pedro", "idade": 25},
            {"nome": "Ana", "idade": 27},
            {"nome": "Rafael", "idade": 28},
        )

        cursor.executemany(sql, data2)  # type: ignore
        connection.commit()
    with connection.cursor() as cursor:
        sql = (
            f"SELECT * FROM {TABLE_NAME} "
        )

        cursor.execute(sql)
        dat = cursor.fetchall()
        for row in dat:
            print(row)
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )

        cursor.execute(sql, (2,))
        connection.commit()
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        for row in cursor.fetchall():
            print(row)
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = %s, idade = %s '
            'WHERE id = %s'
        )

        cursor.execute(sql, ('Mateus', 90, 4))
        connection.commit()
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        for row in cursor.fetchall():
            print(row)
