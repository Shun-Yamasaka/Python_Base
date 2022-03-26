# ラムダを使う
# [ lambda 引数:式 ]
data = [1, 2, 3, 4, 5]

for d in map(lambda x: x*2, data): # 無名関数とリストをmap()関数で組み合わせる
    print(d)