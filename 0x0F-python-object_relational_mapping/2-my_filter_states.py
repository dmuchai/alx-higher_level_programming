#!/usr/bin/python3
"""a script that filters states by user input"""
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

    query = (
            "SELECT * FROM states WHERE name LIKE BINARY '{}' "
            "ORDER BY id ASC;".format(argv[4])
            )
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
