# リストの要素を組み合わせる
city = ["東京", "名古屋", "大阪", "京都"]
sale = [80, 60, 22, 50, 75]

print("都市名データは", city, "です。")
print("売上データは", sale, "です。")

print("データを組み合わせる")

for d in zip(city, sale): # 2つのリストの要素の値が組み合わせられる
    print(d)

print("データとインデックスを組み合わせる")

for d in enumerate(city): # 要素の値とインデックスを組み合わせる
    print(d)