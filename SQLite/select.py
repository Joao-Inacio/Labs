import sqlite3

from CriandoDB import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id, name, weigh = row
    print(_id, name, weigh)

cursor.close()
connection.close()
