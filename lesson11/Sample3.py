# 文字列で検索する
import sqlite3

conn = sqlite3.connect("pdb.db")

c = conn.cursor()

# 固定文字列で検索
itr = c.execute("SELECT * FROM product WHERE name='鉛筆'")

for row in itr:
    print(row)

conn.close()