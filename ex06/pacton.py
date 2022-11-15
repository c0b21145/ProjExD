import pygame as pg
import sys
import random
from random import randint #加藤結衣
import copy

#追加1
WINDOW = (1600, 900)
MAP=[ #ステージ通路設定 １は壁０は通路
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,0,0,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,1,0,0,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,1,0,0,1,2,2,2,2,2,1],
    [1,1,1,1,1,2,1,0,0,1,2,1,1,1,1,1],
    [1,2,2,2,2,2,1,0,0,1,2,2,2,2,2,1],
    [1,2,1,1,1,1,1,0,0,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,0,0,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
#追加1


# スクリーンに関するクラス　追加
class Screen:
    def __init__(self, title, xytpl):
        #color = ["white", "gray"]

        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(xytpl)
        self.rct = self.sfc.get_rect()
#追加
    def map_draw(self,map):
        x=0
        y=0
        self.sfc.fill((0,0,0))
        for i in map:
            for j in i:
                if j == 2:
                    self.wall=pg.draw.circle(self.sfc,(250,250,0),(x*100+50,y*100+50),10)
                if j == 1:
                    self.wall=pg.draw.rect(self.sfc,(100,100,120),(x*100,y*100,100,100),0)
                if j == 0:
                    pg.draw.rect(self.sfc,(0,0,0),(x*100,y*100,100,100),0)
                x +=1
            else:
                x=0
                y+=1
#追加
        # self.bgi_sfc = pg.image.load("ex05/fig/pg_bg.jpg")
        # self.bgi_rct = self.bgi_sfc.get_rect()
        #self.rct_lst = []
        #for y in range(len(maze_lst)):
            #rct_lst_sub = []
            #for x in range(len(maze_lst[y])):
                #bgi_sfc = pg.Surface((100, 100))
                #pg.draw.rect(bgi_sfc, color[maze_lst[y][x]], (0, 0, 100, 100))
                #rct = bgi_sfc.get_rect()
                #rct.center = (x*100+50, y*100+50)
                # self.bgi_rct = self.bgi_sfc.get_rect()
                #rct_lst_sub.append((bgi_sfc, rct))
    
            #self.rct_lst.append(rct_lst_sub)


    def blit(self):
        # self.sfc.blit(self.bgi_sfc, self.bgi_rct)
        #print(len(self.rct_lst))
        #for sub in self.rct_lst:
        #    for sfc_lst, rct_lst in sub:
        #        # print(sfc_lst, rct_lst)
        self.sfc.blit(self.sfc, self.rct) 
        # print(len(self.rct_lst))
        # for sub in self.rct_lst:
        #     for sfc_lst, rct_lst in sub:
        #         # print(sfc_lst, rct_lst)
        #         self.sfc.blit(sfc_lst,rct_lst)
    
#ここから加藤結衣    
# ドット作成クラス
class Dotto:
    def __init__(self, color, radius, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (radius, radius), radius)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(10, scr.rct.width-10)
        self.rct.centery = randint(10, scr.rct.height-10)
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.blit(scr)

 
# こうかとんがドットを食べるクラス
class Eat:
    def __init__(self, color, dot:Dotto, scr:Screen):
        pg.draw.circle(dot.sfc, color, (5, 5), 5)
        # ドットの色を黒にして、食べたようにみせる
#ここまで加藤結衣


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



#ここから加藤結衣
# スコアを表示するクラス 
class Score:
    def __init__(self, x, y):
        self.font = pg.font.SysFont(None, 40)
        self.score = 0
        (self.x, self.y) = (x, y)

    def draw(self, scr:Screen):
        text = self.font.render("SCORE:"+str(self.score), True, (255, 255, 255))
        scr.sfc.blit(text, (self.x, self.y))
    
    def add_score(self, x):
        self.score += x
#ここまで加藤結衣



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

"""

    # 迷路を表示する関数 第3回から引用
    # def show_maze(self, maze_lst):
    #     color = ["white", "gray"]
    #     for y in range(len(maze_lst)):
    #         for x in range(len(maze_lst[y])):

    #             pg.draw(x*100, y*100, x*100+100, y*100+100, 
    #                                     fill=color[maze_lst[y][x]])
"""

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
    #maze = Maze(16,9)

    scr = Screen("Pacton", (1600, 900))

    # kkt = Bird("C:/Users/C0B21013/Documents/ProjExD2022/ProjExd-1/fig/6.png", 2.0, (800, 400))
    kkt = Bird("ex06/fig/6.png",2.0,(800, 400))
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
    
    #ここから加藤結衣
    #赤色のドットを作成
    dot1 = Dotto((255, 0, 0), 5, scr)
    dot2 = Dotto((255, 0, 0), 5, scr)
    dot3 = Dotto((255, 0, 0), 5, scr)
    dot4 = Dotto((255, 0, 0), 5, scr)
    dot5 = Dotto((255, 0, 0), 5, scr)
    dot6 = Dotto((255, 0, 0), 5, scr)
    dot7 = Dotto((255, 0, 0), 5, scr)
    dot8 = Dotto((255, 0, 0), 5, scr)
    dot9 = Dotto((255, 0, 0), 5, scr)

    score = Score(10, 10)
    #ここまで加藤結衣

    clock = pg.time.Clock()
    while True:
        scr.map_draw(MAP)
        scr.blit() # 背景の作成
        kkt.update(scr)
        # for y in range(len(food_lst)):
        #     for x in range(len(food_lst[y])):
        #         food_lst[y][x].updata(scr)

        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        #ここから加藤結衣
        #ドットを作成、スコアを表示
        dot1.update(scr)
        dot2.update(scr)
        dot3.update(scr)
        dot4.update(scr)
        dot5.update(scr)
        dot6.update(scr)
        dot7.update(scr)
        dot8.update(scr)
        dot9.update(scr)
        score.draw(scr) 

        # こうかとんがドットと重なったら　
        if kkt.rct.colliderect(dot1.rct):
            # ドットを食べる(消す)
            Eat((0, 0, 0), dot1, scr)
            # スコアを1足す
            score.score += 1
            pg.display.update()
        
        if kkt.rct.colliderect(dot2.rct):
            Eat((0, 0, 0), dot2, scr)
            score.score += 1
            pg.display.update()

        if kkt.rct.colliderect(dot3.rct):
            Eat((0, 0, 0), dot3, scr)
            score.score += 1
            pg.display.update()

        if kkt.rct.colliderect(dot4.rct):
            Eat((0, 0, 0), dot4, scr)
            score.score += 1
            pg.display.update()

        if kkt.rct.colliderect(dot5.rct):
            Eat((0, 0, 0), dot5, scr)
            score.score += 1
            pg.display.update()

        if kkt.rct.colliderect(dot6.rct):
            Eat((0, 0, 0), dot6, scr)
            score.score += 1
            pg.display.update()

        if kkt.rct.colliderect(dot7.rct):
            Eat((0, 0, 0), dot7, scr)
            score.score += 1
            pg.display.update()

        if kkt.rct.colliderect(dot8.rct):
            Eat((0, 0, 0), dot8, scr)
            score.score += 1
            pg.display.update()
        
        if kkt.rct.colliderect(dot9.rct):
            Eat((0, 0, 0), dot9, scr)
            score.score += 1
            pg.display.update()
        #ここまで加藤結衣

        # 関友斗
        #以下ゲームオーバー画面
        gameover_key = pg.key.get_pressed()
        if gameover_key[pg.K_g] == True:
            scr.sfc.fill((0,0,0)) #画面の色を黒にする 
            fonto = pg.font.Font(None, 200) #Game Overを表示
            moji = "Game Over"
            txt = fonto.render(str(moji),True,(255,0,0))
            scr.sfc.blit(txt, (400,450))

            pg.display.update()
            clock.tick(0.5)
            return

        pg.display.update() #練習2
        clock.tick(1000)    


if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲーム本体
    pg.quit() # 初期化の解除
    sys.exit()