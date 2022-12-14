import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):#３問目
    btn = event.widget
    txt = btn["text"]
    # tkm.showinfo(txt,f"{txt}のボタンが押されました")
    entry.insert(tk.END,txt)

def equal(event):
    eq = entry.get()
    ev = eval(eq)
    entry.delete(0,tk.END)
    entry.insert(tk.END,ev)

def exit():# 最終確認用関数
    check = tkm.askyesno(title="最終確認",
                        message="保存されていないものは消えてしまいますがよろしいですか？\n保存できないけど"
                        )
    if check == True:
        root.destroy()

# 入力された文を削除する
def delete(event):
    entry.delete(0,tk.END)

# 入力された文から一つ文字を削除する
def back_space(event):
    txt = entry.get()
    entry.delete(len(txt)-1,tk.END)

# 枠組みを作成する
root = tk.Tk()
root.geometry("400x500")#１門目
root.protocol("WM_DELETE_WINDOW",exit)

entry = tk.Entry(root,width=10,font=(", 40"),justify="right")#４問目
entry.grid(row=0, column=0, columnspan=3)

# ボタンの作成
number = list(range(9,-1,-1)) #0~9の数を生成
kigo = ["+"]
for i, num in enumerate(number+kigo,0):#２問目
    button = tk.Button(root,text=f"{num}",font=("",30),width=4,height=2)
    # button.pack()
    button.bind("<1>", button_click)
    if i < 3:
        button.grid(row=1, column=i)
    elif i < 6:
        button.grid(row=2, column=i%3)
    elif i < 9:
        button.grid(row=3, column=i%3)
    else:
        button.grid(row=4, column=i%3)

# "="ボタンの作成
button = tk.Button(root,text=f"=",font=("",30),width=4,height=2)
button.bind("<1>",equal)
button.grid(row=4, column=2)

# デリートボタンの作成
button = tk.Button(root,text=f"c",font=("",30),width=4,height=2)
button.bind("<1>",delete)
button.grid(row=2, column=3)

# バックスペースボタンの作成
button = tk.Button(root,text=f"<=",font=("",30),width=4,height=2)
button.bind("<1>",back_space)
button.grid(row=1, column=3)

root.mainloop()