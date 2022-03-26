# 日付を扱う
import datetime

dt = datetime.datetime.now() # 現在日付を取得します
print("現在は", dt, "です")
print("年：", dt.year)
print("月：", dt.month)
print("日：", dt.day)
dt = dt + datetime.timedelta(days=1) # 日付の加算を行う
print("1日後は", dt, "です")