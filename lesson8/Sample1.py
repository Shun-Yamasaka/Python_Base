# クラスを利用する
class Person: # クラスを定義
    def getName(self): # メソッドを定義
        return self.name # データ属性を表すにはselfをつける

    def getAge(self):
        return self.age

pr = Person() # インスタンスを作成
# データ属性に値を代入する
pr.name = "鈴木"
pr.age = 23

# メソッドを呼び出す
n = pr.getName()
a = pr.getAge()

print(n, "さんは", a, "歳です。")