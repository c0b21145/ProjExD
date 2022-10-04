import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

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



root = tk.Tk()
root.geometry("300x500")#１門目

entry = tk.Entry(root,width=10,font=(", 40"),justify="right")#４問目
entry.grid(row=0, column=0, columnspan=3)

number = list(range(9,-1,-1))
kigo = ["+"]
for i, num in enumerate(number+kigo,0):#２問目
    button = tk.Button(root,text=f"{num}",font=("",30),width=4,height=2)
    # button.pack()
    if i < 3:
        button.bind("<1>", button_click)
        button.grid(row=1, column=i)
    elif i < 6:
        button.bind("<1>", button_click)
        button.grid(row=2, column=i%3)
    elif i < 9:
        button.bind("<1>", button_click)
        button.grid(row=3, column=i%3)
    else:
        button.bind("<1>", button_click)
        button.grid(row=4, column=i%3)

button = tk.Button(root,text=f"=",font=("",30),width=4,height=2)
button.bind("<1>",equal)
button.grid(row=4, column=2)
root.mainloop()