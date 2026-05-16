#!/usr/bin/python3
"""takes in the name of a state as
an argument and lists all cities of that state"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s ORDER BY cities.id ASC""", (sys.argv[4],)
    )
    cities = cursor.fetchall()
    for i in range(0, len(cities)):
        print(cities[i][0], end="")
        if i != len(cities) - 1:
            print(", ", end="")
    print()
    cursor.close()
    db.close()
