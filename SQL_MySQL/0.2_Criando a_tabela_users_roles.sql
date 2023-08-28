-- Active: 1691416914754@@127.0.0.1@3306@base_de_dados
CREATE TABLE users_roles (
    user_id INT UNSIGNED NOT NULL,
    role_id INT UNSIGNED NOT NULL,
    CONSTRAINT users_roles_PK PRIMARY KEY (user_id, role_id),
    CONSTRAINT users_roles_FK FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT users_roles_FK_1 FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE ON UPDATE CASCADE
)

