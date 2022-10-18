from email.mime import image
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    # root.geometry("1500x900")

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    tori = tk.PhotoImage(file="ex03/fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx,cy,image=tori,tag="tori")

    key = "" # 現在押されているキーを表す変数

    root.mainloop()