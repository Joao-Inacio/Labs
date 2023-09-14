-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados
# SELECT de mais de uma tabela
SELECT u.id as uid, p.id as pid, u.first_name
FROM users as u, profiles as p
WHERE u.id = p.user_id;