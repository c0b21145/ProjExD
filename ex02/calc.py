import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}のボタンが押されました")

root = tk.Tk()
root.geometry("300x500")

for i, num in enumerate(range(9,-1,-1),0):
    button = tk.Button(root,text=f"{num}",font=("",30),width=4,height=2)
    # button.pack()
    if num > 6:
        button.bind("<1>", button_click)
        button.grid(row=0, column=i)
    elif num > 3:
        button.bind("<1>", button_click)
        button.grid(row=1, column=i%3)
    elif num > 0:
        button.bind("<1>", button_click)
        button.grid(row=2, column=i%3)
    else:
        button.bind("<1>", button_click)
        button.grid(row=3, column=0)


root.mainloop()