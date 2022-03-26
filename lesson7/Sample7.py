# 複数の戻り値を返す
def sell():
    y=2018
    m=10
    d=1
    print(y, "年", m, "月", d, "日に販売が行われました")

    # 複数の戻り値を指定
    return y, m, d

sy, sm, sd = sell() # 複数の戻り値を1つのタプルとして戻している

print("販売完了:", sy, sm, sd)