import random
import datetime

def shutudai():
    Q = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    A = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
    q = random.randint(0,2)
    print(Q[q])
    return q,A

def kaito(number,a):
    ans = str(input("回答を入力してください："))
    # st = datetime.datetime.now()
    if ans in a[number]:
        print("正解")
        # ed = datetime.datetime.now()
        # print((ed-st).seconds)
    else:
        print("不正解")
        # ed = datetime.datetime.now()
        # print((ed-st).seconds)

q,A = shutudai()
kaito(q,A)