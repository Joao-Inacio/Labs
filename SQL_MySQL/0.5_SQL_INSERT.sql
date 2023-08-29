-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados
# Visualizando as tabelas do banco de dados
SHOW TABLES;

# Descreve as colunas da tabela 
DESCRIBE users;

# Inserindo registros na base de dados
INSERT INTO users (
    first_name, last_name, email, password_hash
) VALUES (
    "João", "Inácio", "joao@email.com", "j_hash"
);

# Inserindo vários registros na base de dados
INSERT INTO users (
    first_name, last_name, email, password_hash
) VALUES (
    "Maria", "Clara", "maria@email.com", "m_hash"
), (
    "Pedro", "Silva", "pedro@email.com", "p_hash"
), (
    "Lucas", "Santos", "lucas@email.com", "l_hash"
);
