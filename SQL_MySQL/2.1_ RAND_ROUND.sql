-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados
# Criando a coluna de salário 
ALTER TABLE base_de_dados.users ADD salary DECIMAL(15, 2) NULL;

# Gerando salários aleatórios
UPDATE users SET salary = ROUND(RAND() * 10000, 2);

SELECT * FROM users;
