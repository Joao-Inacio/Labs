-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados
# Left JOIN
SELECT u.id as uid, p.id as pid, u.first_name
FROM users as u
LEFT JOIN profiles as p
ON u.id = p.user_id;