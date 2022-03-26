# リスト使用の注意
# リストへの代入
data1 = [1, 2, 3, 4, 5]
data2 = data1 # リストを表す変数に単純な代入を行う

print("data1は", data1, "です。")
print("data2は", data2, "です。")

data1[0] = 10 # 片方のリストの値を変更すると

print("data1を変更します。")

print("data1は", data1, "です。") #[10, 2, 3, 4, 5]
# もう片方のリストも変更されてしまう。
print("data2は", data2, "です。") #[10, 2, 3, 4, 5]
