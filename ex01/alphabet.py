import random
import datetime

choose_num = 0
chipped_num = 0
loop_Max = 0
 
def syutudai():
    choose_num = random.randint(8,12)
    chipped_num = random.randint(2,4)
    # alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabet = []
    for i in range(26):
        alphabet.append(chr(65+i))
    st = datetime.datetime.now()
    q = random.sample(alphabet,choose_num)
    a = random.sample(q,chipped_num)
    t = [toi for toi in q if toi not in a]
    print("対象文字：",q)
    print("欠損文字：",a) #確認用
    print("表示文字：",t)
    return st,a

def kaito(st,a):
    q = 0
    loop_Max = len(a) + 3
    for i in range(loop_Max):
        if q == 0:
            ans = int(input("欠損文字は幾つありますか？："))
            if ans == len(a):
                q = 1
        else:
            if a == []:
                print("正解です")
                ed = datetime.datetime.now()
                print((ed-st))
                break
            ans = str(input(f"{q}つ目の文字を入力してください："))
            if ans in a:
                q += 1
                a.remove(ans)
            else:
                print("不正解")
    if q < len(a):
        print("もう一度挑戦しよう！")

if __name__ == "__main__":
    st, a = syutudai()
    kaito(st,a)
