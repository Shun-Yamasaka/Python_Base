# CSVファイルを読み込む
import csv # csvモジュールをインポート

f = open("Sample.csv", "r") # csvファイルを読み込む

rd = csv.reader(f) # リーダーを取得

for row in rd: # 1行取り出し
    for col in row: # その中の列項目1つを取り出し
        print(col, end="") # 表示
    print()
f.close() # ファイルクローズ

