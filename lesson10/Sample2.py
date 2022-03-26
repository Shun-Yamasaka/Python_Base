
#with open("Sample.txt", "w") as f: # オープンしたファイルは必ずクローズされる
#    f.write("こんばんは")

# テキストファイルを読み込む
f = open("Sample.txt", "r") # ファイルを読み込みモードでオープンする

lines = f.readlines() # 全ての行を読み出す

# 1行ずつ繰り返して
for line in lines:
    print(line, end="") # 表示する

f.close() # ファイルクローズ