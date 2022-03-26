# 派生クラスを利用する
# 継承とオーバーライド

class Person: # 基底クラスの定義
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Customer(Person): # 派生クラスの定義
    def __init__(self, nm, ag, ad, tl):
        super().__init__(nm, ag)

        self.adr = ad
        self.tel = tl

    def getName(self): # 追加するメソッド
        return "顧客：" + self.name

    def getAdr(self):
        return self.adr

    def getTel(self): # 追加するメソッド
        return self.tel

pr = Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")

# 派生クラスのメソッドが呼び出されている
nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, "さんは", ag, "歳です") 
print("アドレスは", ad, "電話番号は", tl, "です")
