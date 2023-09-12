-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados
SELECT id, first_name, email as uemail
FROM users
WHERE id BETWEEN 50 AND 100
ORDER BY first_name;