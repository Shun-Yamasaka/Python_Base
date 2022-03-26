# URLをオープンする
import urllib.request

# URLを指定してオープン
page = urllib.request.urlopen("https://www.python.org/")

html = page.read() # 読み込みを行う
str = html.decode() # 文字列に変換

print(str) # 表示（HTMLが表示される）