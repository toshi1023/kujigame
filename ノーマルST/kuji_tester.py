import kuji_method
import sys

# キーボード入力によって確率をセット
nomal_print = input('通常時の確率を数字で入力してください>> ')
high_print = input('高確率時の確率を数字で入力してください>> ')
rate = input('超大当たり比率の割合(%)を数字で入力してください>> ')
money1_print = input('超大当たりの出玉を数字で入力してください>> ')
money2_print = input('大当たりの出玉を数字で入力してください>> ')
st_print = input('STの回転数を数字で入力してください>> ')
judge_print = input('ST突入率の割合を数字で入力してください>> ')

print("問題がなければ、Enterキーを押してください（入力しなおす場合は\"no\"を入力してください）")

# シミュレーション開始処理に使用するオブジェクト
start = input()

# "no"を入力すれば確率の入力がやり直し出来るように設定
while True:
    if start != "":
        print("\n\n")
        nomal_print = input('通常時の確率を数字で入力してください>> ')
        high_print = input('高確率時の確率を数字で入力してください>> ')
        rate = input('超大当たり比率の割合(%)を数字で入力してください>> ')
        money1_print = input('超大当たりの出玉を数字で入力してください>> ')
        money2_print = input('大当たりの出玉を数字で入力してください>> ')
        st_print = input('STの回転数を数字で入力してください>> ')
        judge_print = input('ST突入率の割合を数字で入力してください>> ')

        print("問題がなければ、Enterキーを押してください（入力しなおす場合は\"no\"を入力してください）")
        start = input()

    elif start == "":
        # 確率分母のセット（int()で数値化をしないとエラーになる！）
        nomal_rate = int(nomal_print)
        high_rate = int(high_print)
        rate = int(rate)
        money1_rate = int(money1_print)
        money2_rate = int(money2_print)
        st_times = int(st_print)
        judge_rate = int(judge_print)

        # breakしないと以下の関数実行に移らない
        break


# 関数をオブジェクト化
test_nomal = kuji_method.pac_1(nomal_rate)
test_number = kuji_method.pac_2(judge_rate, high_rate, st_times, nomal_rate, rate)
test_loop = kuji_method.pac_3(high_rate, st_times)
result = kuji_method.pac_4(money1_rate, money2_rate)
