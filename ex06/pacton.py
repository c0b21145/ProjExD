import pygame as pg
import sys
import random
import copy

# スクリーンに関するクラス
class Screen:
    def __init__(self, title, xytpl, maze_lst):
        color = ["white", "gray"]
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(xytpl)
        # self.rct = self.sfc.get_rect()
        # self.bgi_sfc = pg.image.load("ex05/fig/pg_bg.jpg")
        # self.bgi_rct = self.bgi_sfc.get_rect()
        self.rct_lst = []
        for y in range(len(maze_lst)):
            rct_lst_sub = []
            for x in range(len(maze_lst[y])):
                bgi_sfc = pg.Surface((100, 100))
                pg.draw.rect(bgi_sfc, color[maze_lst[y][x]], (0, 0, 100, 100))
                rct = bgi_sfc.get_rect()
                rct.center = (x*100+50, y*100+50)
                # self.bgi_rct = self.bgi_sfc.get_rect()
                rct_lst_sub.append((bgi_sfc, rct))
    
            self.rct_lst.append(rct_lst_sub)


    def blit(self):
        # self.sfc.blit(self.bgi_sfc, self.bgi_rct)
        print(len(self.rct_lst))
        for sub in self.rct_lst:
            for sfc_lst, rct_lst in sub:
                # print(sfc_lst, rct_lst)
                self.sfc.blit(sfc_lst,rct_lst)
    

# こうかとんに関するクラス
class Bird:

    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
        }

    def __init__(self, img, zoom, xytpl):
        sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xytpl

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
        self.blit(scr)


# 迷路に関するクラス
class Maze:
    # 迷路を作成する関数 第3回から引用
    def __init__(self, yoko, tate):
        XP = [ 0, 1, 0, -1]
        YP = [-1, 0, 1,  0]
        self.maze_lst = []
        for y in range(tate): # マップの作製
            self.maze_lst.append([0]*yoko)
        for x in range(yoko): # 上下の壁の作成
            self.maze_lst[0][x] = 1
            self.maze_lst[tate-1][x] = 1
        for y in range(tate): # 左右の壁の作成
            self.maze_lst[y][0] = 1
            self.maze_lst[y][yoko-1] = 1
        for y in range(2, tate-2, 2):
            for x in range(2, yoko-2, 2):
                self.maze_lst[y][x] = 1
        for y in range(2, tate-2, 2):
            for x in range(2, yoko-2, 2):
                if x > 2: rnd = random.randint(0, 2)
                else:     rnd = random.randint(0, 3)
                self.maze_lst[y+YP[rnd]][x+XP[rnd]] = 1


    # 迷路を表示する関数 第3回から引用
    # def show_maze(self, maze_lst):
    #     color = ["white", "gray"]
    #     for y in range(len(maze_lst)):
    #         for x in range(len(maze_lst[y])):

    #             pg.draw(x*100, y*100, x*100+100, y*100+100, 
    #                                     fill=color[maze_lst[y][x]])
   

# 道に落ちている食べ物に関するクラス
class Food:
    def __init__(self, color, radius, xytpl):
        self.flag = False
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 食べ物用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx, self.rct.centery = xytpl

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def updata(self, scr):
        self.blit(scr)

    def set_food(self, lst, x, y, scr:Screen):
        if lst[y][x] == 0:
            self.flag = True
            self.blit(scr)

    def remove_food(self, color):
        self.flag = False
        self.sfc.set_colorkey(color)




def main():
    maze = Maze(16,9)

    scr = Screen("Pacton", (1600, 900), maze.maze_lst)

    kkt = Bird("ex06/fig/6.png", 2.0, (900, 400))
    # food_lst = copy.deepcopy(maze.maze_lst)
    # for y in range(len(maze.maze_lst)):
    #     for x in range(len(maze.maze_lst[y])):
    #         food_lst[y][x] = Food((255,255,0), 10, (x,y))
            
    # for y in range(len(food_lst)):
    #     for x in range(len(food_lst[y])):
    #         food_lst[y][x].set_food(maze.maze_lst, x, y ,scr)
    # for y in range(len(food_lst)):
    #     for x in range(len(food_lst[y])):
    #         print(food_lst[y][x].flag)
    
    clock = pg.time.Clock()
    while True:
        scr.blit() # 背景の作成
        kkt.update(scr)
        # for y in range(len(food_lst)):
        #     for x in range(len(food_lst[y])):
        #         food_lst[y][x].updata(scr)

        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return


        pg.display.update() #練習2
        clock.tick(1000)    


if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲーム本体
    pg.quit() # 初期化の解除
    sys.exit()