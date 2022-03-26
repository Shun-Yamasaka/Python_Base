# 例外処理を行う
try:
    f = open("Sample.txt", "r")
except FileNotFoundError: # ファイルオープンできない例外が発生した場合にこのブロックが処理される
    print("ファイルをオープンできませんでした")

else: # 例外が発生しなかった場合はelseブロックを処理する
    lines = f.readlines()
    for line in lines:
        print(line, end="")
    f.close()

finally: # 例外の発生にかかわらず、finallyブロックが処理される
    print("処理を終了する")