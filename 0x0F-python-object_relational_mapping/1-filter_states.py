#!/usr/bin/python3

"""
This script lists all the states with a
`name` starting with the letter 'N' from the
database `hbtn_0e_0_usa`
"""

import MySQLdb as db
from sys import argv

"""
Access to the databse and get the states
from the database.
"""

if __name == '__main__':
    db_connect = db.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()


    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    for row in rows_selected:
        print (row)
