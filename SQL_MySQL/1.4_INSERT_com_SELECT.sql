-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados
# INSERT SELECT = insere valores de uma tabela para outra
INSERT INTO profiles 
(bio, description, user_id)
SELECT
CONCAT('Bio de ', first_name),
CONCAT('Description de ', first_name),
id 
FROM users;