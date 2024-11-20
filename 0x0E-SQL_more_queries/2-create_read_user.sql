-- Script creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates the user user_0d_2 whose password is set to user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- The user_0d_2 password set to user_0d_2_pwd
ALTER USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- GRANT only SELECT privilege to user_0d_2 in the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Apply the privilege changes
FLUSH PRIVILEGES;

