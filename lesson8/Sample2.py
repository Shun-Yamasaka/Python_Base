# 複数のインスタンスを作成する

class Person: # クラスを定義
    def getName(self): # メソッドを定義
        return self.name # データ属性を表すにはselfをつける

    def getAge(self):
        return self.age

pr1 = Person() # 1人目を表すインスタンスを作成
# データ属性に値を代入する
pr1.name = "鈴木"
pr1.age = 23
# メソッドを呼び出す
n1 = pr1.getName()
a1 = pr1.getAge()

pr2 = Person() # 2人目を表すインスタンスを作成
# データ属性に値を代入する
pr2.name = "佐藤"
pr2.age = 38
# メソッドを呼び出す
n2 = pr2.getName()
a2 = pr2.getAge()

print(n1, "さんは", a1, "歳です。") # 1人目の情報を出力
print(n2, "さんは", a2, "歳です。") # 2人目の情報を出力