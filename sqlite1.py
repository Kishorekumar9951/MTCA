import sqlite3 as lite
con=lite.connect('pythonpractice.27.db')
cur=con.cursor()
cur.execute("SELECT * FROM Cars")
rows=cur.fetchone()
for i in rows:
    print(rows)

#for row in rows:
#    print("{0:3}|{1:<15}|{2:>5}".format(row[0],row[1],row[2]))
