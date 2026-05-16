#!/usr/bin/python3
"""displays all values where name matches the argument."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = '{n}'".format(n=sys.argv[4])
    )

    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
