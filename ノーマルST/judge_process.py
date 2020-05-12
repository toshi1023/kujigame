from time import sleep
import random

# 分岐演出のクラスファイル

# congulatulationsの変数を後の条件分岐に使用するため、Noneをセット
congulatulations = None

def judgement(rates):

    # kuji_method.pyで条件分岐の判別要素に使うため、グローバル化
    global congulatulations

    sleep(2)
    print("challenge time\n")
    sleep(3)
    print("＜＜Enterキーを押して\"congulatulations!!!\"が出れば、スペシャルタイム（確率変動）突入!!＞＞\n")
    sleep(3)
    print("突入率は" + str(rates) + "%!!\n")
    sleep(3)
    print("突入の期待度は...？\n")
    sleep(3)

    # 乱数を変数rにセット
    r = random.randint(1, 100)

    # 分岐の%数値を変数に格納
    rate = rates

    # rの値によってセリフ配分を分岐
    if r <= rate:
        if r <= 10:
            print("＜＜ 超激熱です！！！ ＞＞\n")
        elif 10 < r <= rate:
            serif1 = random.randint(1, 100)
            if serif1 <= 35:
                print("＜＜ 激熱です！！ ＞＞\n")
            elif 36 < serif1 <= 70:
                print("＜＜ チャンスです！ ＞＞\n")
            elif 71 < serif1 <= 85:
                print("＜＜ チャンス...？ ＞＞\n")
            elif 86 < serif1 <= 100:
                print("＜＜ 期待はしていいかと... ＞＞\n")
    elif r > rate:
        serif2 = random.randint(1, 100)
        if serif2 <= 15:
            print("＜＜ 激熱です！！ ＞＞\n")
        elif 16 < serif2 <= 40:
            print("＜＜ チャンスです！ ＞＞\n")
        elif 41 < serif2 <= 70:
            print("＜＜ チャンス...？ ＞＞\n")
        elif 71 < serif2 <= 100:
            print("＜＜ 期待はしていいかと... ＞＞\n")

    sleep(3)
    print("ジャッジメント!!!\n")
    sleep(3)
    print("3\n")
    sleep(1.5)
    print("2\n")
    sleep(1.5)
    print("1\n")
    sleep(1.5)
    print("気合を入れてEnterキーを押せ！！！！\n")

    # Enterキーの入力メソッドをインスタンス化
    get_key = input()

    if get_key == "":
        sleep(1)
        if r <= rate:
            congulatulations = "Congulatulations!!!\n"
            print(congulatulations)
            sleep(3)
            print("スペシャルタイム突入！！！\n")
            sleep(3)

        else:
            print("You Failure...\n")
            sleep(3)
            print("チャンスタイム突入！\n")
            sleep(3)

# ここまでがjudgement()関数の内容
