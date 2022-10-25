import pygame as pg
import sys


def main():
    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((800,600))

    tori_sfc = pg.image.load("fig/6.png") # surface
    tori_rct = tori_sfc.get_rect() # rect
    tori_rct.center = 700, 400
    scrn_sfc.blit(tori_sfc, tori_rct) # スクリーンにこうかとんを貼り付ける

    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(0.2)


if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()