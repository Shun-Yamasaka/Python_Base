# 関数をリストに代入する
def append():
    print("データを追加します")
def update():
    print("データを変更します")
def delete():
    print("データを削除します")

list = [append, update, delete] # 関数をリストの要素にする

res = int(input("操作番号を入力してください(0〜2)"))

if 0 <= res and res < len(list):
    list[res]() # リストの要素として関数を呼び出す
else:
    print("対象外です")