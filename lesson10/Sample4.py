# JSONファイルを読み込む
import json # jsonモジュールをインポートする

f = open("Sample.json", "r") # jsonファイルをオープンする

data = json.load(f) # jsonファイルを読み込む

print(data) # 読み込んだデータを表示する

f.close()
