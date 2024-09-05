-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS SCS_test_db;
CREATE USER IF NOT EXISTS 'SCS_test'@'localhost' IDENTIFIED BY 'SCS_test_pwd';
GRANT ALL PRIVILEGES ON `SCS_test_db`.* TO 'SCS_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'SCS_test'@'localhost';
FLUSH PRIVILEGES;
