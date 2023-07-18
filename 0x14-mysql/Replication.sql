-- Access MySQL on web-01 as root
CREATE USER 'replica_user'@'%' IDENTIFIED BY '1234pwd'; -- Create new user replica_user with the desired password and host set to '%'
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%'; -- Grant appropriate permissions for replication to replica_user
FLUSH PRIVILEGES; -- Apply the changes

-- Grant SELECT privileges on mysql.user table to holberton_user
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES; -- Apply the changes

CHANGE MASTER TO MASTER_HOST = '54.160.120.43', MASTER_USER = 'replica_user', MASTER_PASSWORD = '1234pwd', MASTER_LOG_FILE = ' mysql-bin.000009', MASTER_LOG_POS = 107;
