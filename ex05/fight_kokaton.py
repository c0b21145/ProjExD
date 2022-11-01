import pygame as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


class Screen:
    
    def __init__(self, title, xytpl, bgimg):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(xytpl)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg)
        self.bgi_rct = self.bgi_sfc.get_rect()
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


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
                # 練習7
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb:
    
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Shot:

    def __init__(self, color, radius, vy, scr:Bird):
        self.sfc = pg.Surface((radius*2, radius*2))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (radius, radius), radius)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = scr.rct.centerx
        self.rct.centery = scr.rct.centery
        self.vy = vy
        self.flag = False
    
    def blit(self, scr:Bird):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Bird):
        self.rct.move_ip(0,self.vy)
        # yoko, tate = check_bound(self.rct, scr.rct)
        # self.vy *= tate
        self.blit(scr)
        if self.rct.top < 0:
            self.flag = False
            self.reload(scr)

    def reload(self, scr:Bird):
        self.rct.centerx = scr.rct.centerx
        self.rct.centery = scr.rct.centery
        

class Zanki:

    def __init__(self, zanki:int):
        self.zanki = zanki
        self.font = pg.font.Font(None, 20)

    def __sub__(self, other):
        return self.zanki - other

    def hit(self, obj:Bomb):
        obj.vx *= -1
        obj.vy *= -1
        

def main():
    # スクリーンを作成
    scr = Screen("負けるな！こうかとん", (1600, 900),"ex05/fig/pg_bg.jpg")
    
    # こうかとんを作成
    kkt = Bird("ex05/fig/6.png", 2.0, (900, 400))
    
    # 爆弾を作成
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)

    sht = Shot((0,255,0), 40, -1, kkt)

    znk = Zanki(5)
    
    clock = pg.time.Clock() # 練習1
    while True:
        # 背景の作成
        scr.blit()
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return
        key_states = pg.key.get_pressed()
        if key_states[pg.K_SPACE]:
            # print("hoge")
            sht.flag = True

        # こうかとんの座標を更新
        kkt.update(scr)
    
        # 爆弾の更新
        bkd.update(scr)

        if sht.flag is False:
            sht.reload(kkt)
        else:
            sht.update(scr)
    
        if sht.rct.colliderect(bkd.rct):
            sht.flag = False

        # 練習8
        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            znk.zanki -= 1
            znk.hit(bkd)
            if znk.zanki == 0:
                return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
