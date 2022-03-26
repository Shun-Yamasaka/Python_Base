import sqlite3 # データベースを利用するためのモジュールをインポートする

conn = sqlite3.connect("pdb.db") # データベースに接続する

c = conn.cursor() # カーソルを取得

c.execute("DROP TABLE IF EXISTS product")

# 表を作成する
c.execute("CREATE TABLE product(name CHAR(20), price INT)")
# データを追加する
c.execute("INSERT INTO product VALUES('鉛筆', 80)")
c.execute("INSERT INTO product VALUES('消しゴム', 50)")
c.execute("INSERT INTO product VALUES('定規', 200)")
c.execute("INSERT INTO product VALUES('コンパス', 300)")
c.execute("INSERT INTO product VALUES('ボールペン', 100)")

conn.commit() # コミットする

itr = c.execute("SELECT * FROM product") # 表のデータを取り出す

for row in itr:
    print(row)

conn.close()