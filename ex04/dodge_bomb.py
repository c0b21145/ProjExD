import pygame as pg
import sys


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))

    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg") # 背景
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("ex04/fig/6.png") # surface
    tori_sfc = pg.transform.rotozoom(tori_sfc,0, 2.0)
    tori_rct = tori_sfc.get_rect() # rect
    tori_rct.center = 900, 400


    clock = pg.time.Clock()
    while True:

        scrn_sfc.blit(bg_sfc, bg_rct) # スクリーンに背景を貼り付ける
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        scrn_sfc.blit(tori_sfc, tori_rct) # スクリーンにこうかとんを貼り付ける        

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()