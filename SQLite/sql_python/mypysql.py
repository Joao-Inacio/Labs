import os

import dotenv
import pymysql

dotenv.load_dotenv()

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
            'CREATE TABLE IF NOT EXISTS usuarios ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL , '
            'PRIMARY KEY (id)'
            ') '
        )
        connection.commit()
        print(cursor)
