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
    global mx, my
    global cx, cy
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_data[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori",cx,cy)
    root.after(100,main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    # root.geometry("1500x900")

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_data = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canv,maze_data) # 迷路を表示

    tori = tk.PhotoImage(file="ex03/fig/3.png") # 画像の選択
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx,cy,image=tori,tag="tori") # こうかとんを表示

    key = "" # 現在押されているキーを表す変数

    root.bind("<KeyPress>",key_down)

    root.bind("<KeyRelease>",key_up)

    main_proc()



    root.mainloop()