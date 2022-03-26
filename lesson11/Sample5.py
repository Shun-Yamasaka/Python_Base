import sqlite3

conn = sqlite3.connect("pdb.db")

c = conn.cursor()

itr = c.execute("SELECT * FROM product ORDER BY price DESC") # price列の値が大きい順に並べる

for row in itr:
    print(row)

conn.close()