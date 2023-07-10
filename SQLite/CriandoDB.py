import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL
# Cuidado: ao fazer delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
# Deletando os ID
cursor.execute(
    f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'"
)
connection.commit()

# Criando a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()
# usando placeholders para maior segurança (bindings) no SQLite
sql = (
    f"INSERT INTO {TABLE_NAME} (name, weight) "
    "VALUES (:nome, :peso)"
)
# Regitrando  valores nas colunas da tabelas
# cursor.execute(sql, ['Maria', 59])
# executemany - Inserindo vários valores com placeholders no SQLite
# cursor.executemany(sql, (('Lucas', 78), ('Armando', 72), ('Pedro', 65)))
# execute e executemany com dicionários e lista de dicionários no SQLite
# cursor.execute(sql, {'nome': 'Tito', 'peso': 97})
cursor.executemany(sql, (
    {'nome': 'Tito', 'peso': 97},
    {'nome': 'Neo', 'peso': 79},
    {'nome': 'Manu', 'peso': 85},
    {'nome': 'Lana', 'peso': 78},
    {'nome': 'Bruno', 'peso': 75}
))
connection.commit()

cursor.close()
connection.close()
