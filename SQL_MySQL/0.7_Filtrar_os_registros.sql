-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados
# WHERE filtra registros
SELECT * FROM users WHERE id = 3;

SELECT * FROM users WHERE id < 3 OR first_name = 'João';