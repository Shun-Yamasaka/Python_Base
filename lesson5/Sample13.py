# リストの要素を分解する
city = ["東京", "名古屋", "大阪", "京都"]
sale = [80, 60, 22, 50, 75]

print("都市名データは", city, "です")
print("売上データは", sale, "です")

print("データを組み合わせる")

for d in zip(city, sale): # 2つのリストの要素の値を組み合わせる
    print(d)

print("データを分解する")

for c, s in zip(city, sale): # 組み合わせた要素を分解する
    print("都市名は", c, "売上は", s)