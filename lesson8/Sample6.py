# ファイルを分割する
import myclass # 別モジュールをインポートする

# 別モジュールのクラスを呼び出す
pr = myclass.Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")
nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, "さんは", ag, "歳です")
print("アドレスは", ad, "電話番号は", tl, "です")