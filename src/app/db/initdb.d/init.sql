CREATE DATABASE zvany CHARSET utf8mb4 COLLATE utf8mb4-unicode-ci;

CREATE USER 'zvany'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON zvany.* TO 'zvany'@'localhost';

USE zvany;