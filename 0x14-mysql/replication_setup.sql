---Create database tyrell_corp and switch to it:
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
--Create table nexus6 and add an entry:
CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));
INSERT INTO nexus6 (name) VALUES ('Roy Batty');
--Grant SELECT permission to holberton_user on nexus6
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

