import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker
import random

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    global cx, cy
    # 迷路を移動する
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
    if key == "q":
        exit()
    canv.coords("tori",cx,cy)
    root.after(100,main_proc)

def random_work():
    global ex,ey
    global ecx, ecy
    work = random.randint(1,4)
    if work%4==0:
        ey -= 1
    elif work%4==1:
        ey += 1
    elif work%4==2:
        ex -= 1
    else:
        ex += 1
    if maze_data[ey][ex] == 0:
        ecx, ecy = ex*100+50, ey*100+50
    else:
        if work%4==0:
            ey += 1
        elif work%4==1:
            ey -= 1
        elif work%4==2:
            ex += 1
        else:
            ex -= 1
    canv.coords("e_tori",ecx,ecy)
    root.after(1000,random_work)

def exit():
    check = tkm.askyesno(title="終わりにしますか？",message="止めるのならOKを押してください")
    if check == True:
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    # root.geometry("1500x900")

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_data = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canv,maze_data) # 迷路を表示

    tori_img = [f"ex03/fig/{i}.png" for i in range(10)] # こうかとんの画像のリスト
    con = random.randint(0,9) # 画像変更時のフラグ
    tori = tk.PhotoImage(file=tori_img[con])            
    # tori = tk.PhotoImage(file="ex03/fig/3.png") # 画像の選択
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx,cy,image=tori,tag="tori") # こうかとんを表示

    ex,ey = 4, 4
    ecx, ecy = ex*100+50, ey*100+50
    e_tori = tk.PhotoImage(file=tori_img[con])            
    canv.create_image(cx,cy,image=e_tori,tag="e_tori") # こうかとんを表示

    key = "" # 現在押されているキーを表す変数

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    random_work()

    root.mainloop()