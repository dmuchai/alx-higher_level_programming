#!/usr/bin/python3
"""a script that lists all states with a name starting with N"""
import MySQLdb
from sys import argv

def main():
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

    # Fetch and print all results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
