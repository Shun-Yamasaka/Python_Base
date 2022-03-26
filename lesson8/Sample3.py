# コンストラクタ

class Person:
    # コンストラクタ
    def __init__(self, name, age): # インスタンス作成時に呼び出される
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

pr = Person("鈴木", 23) # インスタンス作成時に値を渡す

n = pr.getName()
a = pr.getAge()

print(n, "さんは", a, "歳です")