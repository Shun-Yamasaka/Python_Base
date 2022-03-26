# システム処理
# ディレクトリの内容を表示
import os

curdir = os.listdir(".") # ディレクトリのリストを取得

for name in curdir: # リストから1つディレクトリ・ファイルを取得
    print(name)