-- A script that creates the MYSQL serv er user user_0d_1

-- creating the user...
CREATE USER If NOT EXISTS 'user_0d_1'@'localhost'

-- set user password to user_0d_1_pwd
IDENTIFIED BY 'user_0d_1_pwd';

-- grant all privileges to user
GRANT ALL PRIVILEGES
ON *.*
TO 'user_0d_1'@'localhost';
