# リストから新しいリストを得る
# リスト内包表記（コンプリヘンション）

data = [1, 2, 3, 4, 5]
print("現在のデータは", data, "です")

# [式 for 変数 in リスト if 条件] (要素を変数に取り出し、条件がTrueであれば、式の値を新しいリストの要素とする)
ndata = [ n*2 for n in data if n!=3 ]
print("新しいデータは", ndata, "です")
