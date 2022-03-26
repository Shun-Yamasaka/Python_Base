# クラスの定義を別モジュール（ファイル）に記述する
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Customer(Person):
    def __init__(self, nm, ag, ad, tl):
        super().__init__(nm, ag) # 基底クラスのデータ属性を初期化するために、基底クラスのコンストラクタを呼び出す

        self.adr = ad
        self.tel = tl

    def getName(self):
        return "顧客：" + self.name
    
    def getAdr(self):
        return self.adr
    
    def getTel(self):
        return self.tel