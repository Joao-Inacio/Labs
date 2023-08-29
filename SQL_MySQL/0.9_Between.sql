-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados
SELECT * FROM users WHERE created_at >= '2019-12-29 01:46:33' AND created_at <= '2020-01-21 07:33:05';

# BETWEEN seleciona dados entre um e outro
SELECT * FROM users WHERE created_at BETWEEN '2019-12-29 01:46:33' AND '2020-01-21 07:33:05';
