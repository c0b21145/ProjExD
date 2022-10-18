print("hello world")

import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    # tkm.showwarning("警告","押すなよ")
    btn = event.widget
    txt =btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

root = tk.Tk()
root.title("テヌト")
root.geometry("500x200")

label = tk.Label(root,
                text="ラベルを書いてみたお",
                font=("",20)
                )
label.pack()

button = tk.Button(root,text="押す",font=("",30),bg="#ffdfdf")
button.bind("<1>",button_click)
button.pack()

entry = tk.Entry(root, width=30)
entry.insert(tk.END,"fugapiyo")
entry.pack()



root.mainloop()
