#!/usr/bin/python3
"""SQL query using parameterized query to prevent SQL injection"""
import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
    cursor.execute(query, (argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
