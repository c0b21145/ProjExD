import pygame as pg
import sys
from random import randint

# key_delta = {
#     pg.K_UP:    [0, -1],
#     pg.K_DOWN:  [0, +1],
#     pg.K_LEFT:  [-1, 0],
#     pg.K_RIGHT: [+1, 0],
# }


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


def main():
    # スクリーンを作成
    scr = Screen("逃げろ！こうかとん", (1600, 900),"ex05/fig/pg_bg.jpg")
    # 練習1
    # pg.display.set_caption("逃げろ！こうかとん")
    # scrn_sfc = pg.display.set_mode((1600, 900))
    # scrn_rct = scrn_sfc.get_rect()
    # bg_sfc = pg.image.load("fig/pg_bg.jpg")
    # bg_rct = bg_sfc.get_rect()

    # こうかとんを作成
    kkt = Bird("ex05/fig/6.png", 2.0, (900, 400))
    # 練習3
    # tori_sfc = pg.image.load("fig/6.png")
    # tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    # tori_rct = tori_sfc.get_rect()
    # tori_rct.center = 900, 400

    # 爆弾を作成
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    # 練習5
    # bomb_sfc = pg.Surface((20, 20)) # 空のSurface
    # bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    # pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # 爆弾用の円を描く
    # bomb_rct = bomb_sfc.get_rect()
    # bomb_rct.centerx = randint(0, scrn_rct.width)
    # bomb_rct.centery = randint(0, scrn_rct.height)
    # vx, vy = +1, +1 # 練習6

    clock = pg.time.Clock() # 練習1
    while True:
        # 背景の作成
        scr.blit()
        # scrn_sfc.blit(bg_sfc, bg_rct) # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        # こうかとんの座標を更新
        kkt.update(scr)
        # key_states = pg.key.get_pressed()
        # for key, delta in key_delta.items():
        #     if key_states[key]:
        #         tori_rct.centerx += delta[0]
        #         tori_rct.centery += delta[1]
        #         # 練習7
        #         if check_bound(tori_rct, scrn_rct) != (+1, +1):
        #             tori_rct.centerx -= delta[0]
        #             tori_rct.centery -= delta[1]
        # scrn_sfc.blit(tori_sfc, tori_rct) # 練習3

        # 爆弾の更新
        bkd.update(scr)
        # 練習7
        # yoko, tate = check_bound(bomb_rct, scrn_rct)
        # vx *= yoko
        # vy *= tate
        # bomb_rct.move_ip(vx, vy) # 練習6
        # scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5

        # 練習8
        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
