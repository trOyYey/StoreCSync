-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS SCS_dev_db;
CREATE USER IF NOT EXISTS 'SCS_dev'@'localhost' IDENTIFIED BY 'SCS_dev_pwd';
GRANT ALL PRIVILEGES ON `SCS_dev_db`.* TO 'SCS_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'SCS_dev'@'localhost';
FLUSH PRIVILEGES;
