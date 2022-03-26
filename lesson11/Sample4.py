# データの一部から検索する
import sqlite3

conn = sqlite3.connect("pdb.db")

c = conn.cursor()

# LIKEを使った一部検索
itr = c.execute("SELECT * FROM product WHERE name LIKE '%ン%'")

for row in itr:
    print(row)

conn.close()