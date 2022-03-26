# HTMLを解析する
import urllib.request
from html.parser import HTMLParser

class SampleHTMLParser(HTMLParser): # HTMMLParserクラスを基底クラスとした派生クラスを定義
    def __init__(self): # コンストラクタを定義
        HTMLParser.__init__(self)
        self.title = False

    def handle_starttag(self, tag, attrs): # HTMLの開始タグを解析するメソッドを定義
        if tag == "title":
            self.title = True

    def handle_data(self, data): # HTML中のデータを取得するメソッドを定義する
        if self.title is True:
            print("タイトル：", data)
            self.title = False

page = urllib.request.urlopen("https://www.python.org/")

html = page.read()
str = html.decode()

p = SampleHTMLParser() # 定義したクラスのインスタンスを作成
p.feed(str) # 読み込んだページを解析する

p.close()