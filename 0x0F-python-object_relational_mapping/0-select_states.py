```#!/usr/bin/python 3
"""The script lists all states from a database"""
import  MySQLdb
Import sys


# Get passed Args
if __name__="__main__":
      user = sys.argv[1]
      password = sys.argv[2]
      database= sys.argv[3]

conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=database, charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
