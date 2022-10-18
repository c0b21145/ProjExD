from email.mime import image
import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canv.coords("tori",cx,cy)
    root.after(100,main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    # root.geometry("1500x900")

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    tori = tk.PhotoImage(file="ex03/fig/3.png") # 画像の選択
    cx, cy = 300, 400

    key = "" # 現在押されているキーを表す変数

    root.bind("<KeyPress>",key_down)

    root.bind("<KeyRelease>",key_up)

    main_proc()

    maze_data = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canv,maze_data) # 迷路を表示
    canv.create_image(cx,cy,image=tori,tag="tori") # こうかとんを表示


    root.mainloop()