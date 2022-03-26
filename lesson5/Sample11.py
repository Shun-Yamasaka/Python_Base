# 逆順にする際の注意
# reversed()関数とreverse()メソッドを使ってリストを逆順にする方法
data = [1, 2, 3, 4, 5]
print("現在のデータは", data, "です。")

print("data[::-1]をfor文で処理する。")
for d in data[::-1]: # スライスで処理する
   print(d) # 逆順による処理が行われるが、
print("data[::-1]は", data[::-1], "です。")
# 元のデータは変更されない
print("現在のデータは", data, "です。")

print("reversed(data)をfor文で処理する")
for d in reversed(data): # reversed()関数で処理する
    print(d)
print("reversed(data)は", reversed(data), "です")
print("現在のデータは", data, "です")

print("data.reverse()を処理します")
data.reverse() # reverseによる逆順にすると
# 元のデータも逆順に変更される
print("現在のデータは", data, "です")
