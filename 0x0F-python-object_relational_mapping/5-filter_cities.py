#!/usr/bin/python3
"""script that takes the name of a state and lists all cities of that state"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")

    cursor.execute(query, (argv[4],))

    cities = cursor.fetchall()

    print(", ".join([city[0] for city in cities]))

    cursor.close()
    db.close()
