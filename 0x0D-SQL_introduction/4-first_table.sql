-This script creates a table called first_table in the current database in your MySQL server
- The database name will be passed as an argument of the mysql command

CREATE first_table IF NOT EXISTS(id INT, name VARCHAR(256))

