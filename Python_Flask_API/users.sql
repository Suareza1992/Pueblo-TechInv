CREATE DATABASE users;

USE users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO users (name, email) VALUES
('Angel', 'angel@email.com'),
('Benito', 'benito@email.com'),
('Carlos', 'carlos@email.com');

