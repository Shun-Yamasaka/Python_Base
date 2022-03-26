# 新しいリストを作成する
data1 = [1, 2, 3, 4, 5]
data2 = list(data1) # リストを新しく作成する

print("data1は", data1, "です。")
print("data2は", data2, "です。")

data1[0] = 10

print("data1を変更します。")

print("data1は", data1, "です。")
# もう片方のリストはそのままの状態になっている
print("data2は", data2, "です。")
