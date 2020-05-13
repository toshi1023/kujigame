import random
import judge_process
from time import sleep

# pac_2()関数で使用する変数をセット
lucky = None
gameover = None
lucky_times = 1
st_lucky_times = 0
st2_lucky_times = 0
rates = 0
num1 = 0

# 以下、通常抽選の内容
def pac_1(nomal):
    cnt = 0

    while True:
        r = random.randint(1, nomal)
        print(r)

        cnt = cnt + 1
        if r == 1:
            break

    print(str(cnt) + "回目で初回大当たりをゲット\n")

# ここまでが関数pac_1の内容


# 以下、ST突入分岐の処理とSTの抽選システムの内容
# judge1=分岐抽選の確率,number=高確率の当たり確率,time=抽選回数,nomal2=低確率の当たり確率, rate=大きい大当たり割合
# num1はpac_3()にてメソッドの引数の値を代入し、pac_2()のループが走った時にelseの処理が動くように設定
def pac_2(judge1, number, time, nomal2, rate):
    if num1 == 0:
        judge = judge1
        judgement = judge_process.judgement(judge)
        congulatulations = judge_process.congulatulations
    # 時短とSTの分岐の時にcongulatulationsの値の有無で判別するため、elseで値の代入を実施
    else:
        congulatulations = "＜＜＜＜　引き戻しに成功！　＞＞＞＞\n"

    times = 0
    times2 = 0
    # 関数外でst_times変数の値を利用するため、グローバル化
    global st_times
    st_times = time
    global gameover
    global lucky
    global lucky_times
    global st_lucky_times
    global st2_lucky_times
    global rates
    rates = rate

    # congulatulationsの値がNoneの時は時短の処理を走らせる
    if congulatulations == None:
        # チャンスタイムの解説＆スタート
        print( "100回転で" + str(nomal2) + "分の1の大当たりを引け！！\n")
        sleep(2)
        while times2 <= 100:
            nomal_time = random.randint(1, nomal2)

            times2 += 1
            if nomal_time == nomal2:
                break
        # while times2 <= 100 のelse条件
        else:
            gameover = "＜＜＜＜　チャンスタイム終了　＞＞＞＞\n"
            print( gameover )
            sleep(2)

        # 何回目の抽選で当たったかをlucky2変数に代入
        lucky2 = times2

        # 100回以内で当たりを引けた場合、pac_2()の処理を走らせる
        # congulatulationsの値を書き換えする
        # →２回目のループ時に時短を再度走らせないようにするため
        if lucky2 <= 100:
            success = "引き戻しに成功！"
            lucky_times += 1
            print("　　　　　　　　　　　　　　　《《》》》")
            print("　　　　　　　　　　　　　　　(。)(。) 》》〉")
            print("　　　　　　　　　　　　　　ノ　　　 ）《《")
            print("　 　　　　　　　　　　　　<＿＿　　 l《《")
            print(success + "  ＞　　   ＿__）　　l》〉")
            print("　　　　　　　　　　　　　<＿_ノ　 /《 \n")
            r = random.randint(1, 100)
            if r <= rates:
                st_lucky_times += 1
                sleep(2)
                print( str(lucky2) + "回目で" + str(st_lucky_times) + "連目の超大当たりをゲット\n" )
            else:
                st2_lucky_times += 1
                sleep(2)
                print( str(lucky2) + "回目で" + str(st2_lucky_times) + "連目の大当たりをゲット\n" )
            sleep(2)
            print("スペシャルタイム突入！！！\n")
            sleep(2)
            print( str(st_times) + "回転で" + str(number) + "分の1の大当たりを引け！！\n")
            sleep(2)

    # 以下、congulatulationsに値が入っていたとき、もしくは時短で引き戻したときに処理を走らせる
    else:
        # 2連目以降からはスペシャルタイムの解説をしない
        if lucky_times < 2:
            # スペシャルタイムの解説＆スタート
            print( str(st_times) + "回転で" + str(number) + "分の1の大当たりを引け！！\n")
            sleep(2)

        while times <= st_times:
            st = random.randint(1, number)

            times += 1
            if st == number:
                break

        # while times <= st_times のelse条件
        # 時短から引き戻しているか否かをgameoverの値の有無で確認
        # 時短から引き戻している場合はこのタイミングでgameoverに値が初めて入る
        else:
            if gameover == None:
                gameover = "＜＜＜＜　スペシャルタイム終了　＞＞＞＞\n"
            print( gameover )
            sleep(2)

        # 何回目の抽選で当たったかをlucky変数に代入
        lucky = times

        if times <= st_times:
            lucky_times += 1
            r = random.randint(1, 100)
            if r <= rates:
                st_lucky_times += 1
                print( str(lucky) + "回目で" + str(st_lucky_times) + "連目の超大当たりをゲット\n")
            else:
                st2_lucky_times += 1
                print( str(lucky) + "回目で" + str(st2_lucky_times) + "連目の大当たりをゲット\n")
            sleep(2)

# ここまでが関数pac_2の内容


# pac_2関数の処理で規定回数以内で当たりを引けていたら繰り返し
# 当たりが引けなかった場合はgameover変数に値が入る → ループを抜け出すトリガー
def pac_3(number1, number2):
    global num1
    num1 = number1
    num2 = number2
    while True:
        if gameover == None:
            # 引数1と引数4は初回時の処理にしか使用しないため、0を設定
            pac_2(0, num1, num2, 0, rates)
            sleep(2)
        else:
            break
            sleep(2)

    print( str(lucky_times) + "回の当たり回数で終了\n")
    sleep(2)

# ここまでが関数pac_3の内容

# 出玉をカウントする処理を以下に記述
def pac_4(money1, money2):
    money1 = st_lucky_times * money1
    money2 = st2_lucky_times * money2

    print("------------  結果  ------------\n")
    print("  超大当たり  x " + str(st_lucky_times) + "回 : " + str(money1) + "発")
    print("  大当たり    x " + str(st2_lucky_times) + "回 : " + str(money2) + "発\n")
    print("--------------------------------")
    sleep(2)
    print("もとに戻してください")

# ここまでが関数pac_4の内容
