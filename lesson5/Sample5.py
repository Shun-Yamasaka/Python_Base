# リスト要素を追加・挿入する
sale = [80, 60, 22, 50, 75]
print("現在のデータは", sale, "です。")

print("末尾に100を追加します。")
sale.append(100) # リストの末尾に値を追加
print("現在のデータは", sale, "です。")

print("sale[2]に25を挿入します。")
sale.insert(2, 25) # リストの指定した位置に値を挿入
print(sale)