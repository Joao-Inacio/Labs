-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados

SELECT * FROM users WHERE first_name LIKE 'a%';

SELECT * FROM users WHERE first_name LIKE '%a%';

SELECT * FROM users WHERE first_name LIKE '%a';

SELECT * FROM users WHERE first_name LIKE '_a%';

SELECT * FROM users WHERE first_name LIKE '____';