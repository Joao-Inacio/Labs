-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados
# Selecionando todos os dados da tabela
SELECT * FROM users;

# Selecionando todos os dados da tabela com alias
SELECT * FROM users AS us;
SELECT * FROM users us;

SELECT us.email uemail, us.first_name FROM users AS us
