# 日付情報をフォーマットする
import datetime

dt = datetime.datetime.now()
str = dt.strftime("%c") # 適切な書式の日時文字列とする

print("現在は", str, "です")

dt = dt + datetime.timedelta(days=1)
str = dt.strftime("%Y-%m-%d") # 西暦-月-日の文字列とする
print("1日後は", str, "です")