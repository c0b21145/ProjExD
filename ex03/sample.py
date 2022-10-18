import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global jid
    if jid != None:
        root.after_cancel(jid)
        jid = None
        return
    # key = event.keysym
    # tkm.showinfo("キー押した",f"{key}が押されました")
    jid = root.after(1000,count_up)

def count_up():
    global tmr,jid
    tmr += 1
    label["text"] = tmr
    jid = root.after(1000, count_up)#1秒毎に数え上げる

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, font=("", 80))
    label.pack()
    
    tmr = 0
    jid = None
    # root.after(1000, count_up)#実行されてから1秒後に開始
    root.bind("<KeyPress>",key_down)

    root.mainloop()
