# 文字列を検索する
str = input("文字列を入力してください")
key = input("検索する文字列を入力してください")

res = str.find(key) # 検索実施

if res != -1:
    print(str, "の", res, "の位置に", key, "が見つかりました")
else:
    print(str, "の中に", key, "が見つかりませんでした")