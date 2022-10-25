import pygame as pg
import sys


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))

    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg") # 背景
    bg_rct = bg_sfc.get_rect()

    clock = pg.time.Clock()
    while True:

    # tori_sfc = pg.image.load("fig/6.png") # surface
    # tori_rct = tori_sfc.get_rect() # rect
    # tori_rct.center = 700, 400
    # scrn_sfc.blit(tori_sfc, tori_rct) # スクリーンにこうかとんを貼り付ける

        scrn_sfc.blit(bg_sfc, bg_rct) # スクリーンに背景を貼り付ける
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()