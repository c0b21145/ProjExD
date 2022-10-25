import pygame as pg
import sys
from random import randint
from random import choice

def check_bound(obj_rct, scr_rct):
    """"
    obj_rct こうかとんrct 又は 爆弾rct
    scr_rct スクリーンrct
    領域内：+1 領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: tate = -1
    return yoko, tate



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg") # 背景
    bg_rct = bg_sfc.get_rect()

    tori_img = [f"ex04/fig/{i}.png" for i in range(10)] # こうかとんの立ち絵を内包するリスト
    tori_sfc = pg.image.load(choice(tori_img)) # surface
    tori_sfc = pg.transform.rotozoom(tori_sfc,0, 2.0)
    tori_rct = tori_sfc.get_rect() # rect
    tori_rct.center = 900, 400

    # 爆弾の作成
    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0, 0, 0)) # 隅の黒いところを透明にする
    # bomb_r, bomb_g, bomb_b = 0, 0, 0 
    bomb_r, bomb_g, bomb_b = 1, 1, 1
    pg.draw.circle(bomb_sfc, (bomb_r, bomb_g, bomb_b), (10, 10), 10) # 円を書く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery = randint(1000, scrn_rct.width), randint(500, scrn_rct.height)
    vx, vy = +1, +1

    # 障害物の作成
    square_sfc = pg.Surface((100, 100))
    square_sfc.set_colorkey((0, 0, 0))
    pg.draw.polygon(square_sfc, (255, 0, 0), [(0,0),(0,100),(100,100),(100,0)])
    square_rct = square_sfc.get_rect()
    square_rct.centerx = randint(0, scrn_rct.width)
    square_rct.centery = randint(0, scrn_rct.height)


    zanki = 5 # 残機の初期値を設定
    znk_sfc = pg.font.Font(None, 40)


    clock = pg.time.Clock()
    while True:

        scrn_sfc.blit(bg_sfc, bg_rct) # スクリーンに背景を貼り付ける
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        scrn_sfc.blit(tori_sfc, tori_rct) # スクリーンにこうかとんを貼り付ける
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]: tori_rct.centery -= 1 # こうかとんを上に移動
        if key_states[pg.K_DOWN]: tori_rct.centery += 1 # こうかとんを下に移動
        if key_states[pg.K_LEFT]: tori_rct.centerx -= 1 # こうかとんを左に移動
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1 # こうかとんを右に移動
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1 :
            if key_states[pg.K_LEFT]:tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:tori_rct.centerx -= 1
        if tate == -1 :
            if key_states[pg.K_UP]:tori_rct.centery += 1
            if key_states[pg.K_DOWN]:tori_rct.centery -= 1
            
        yoko, tate = check_bound(bomb_rct,scrn_rct)            
        vx *= yoko
        vy *= tate

        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) # スクリーンに爆弾を貼り付ける
        bomb_r, bomb_g, bomb_b = bomb_r+1, bomb_g+2, bomb_b+3
        if bomb_r > 255: bomb_r = 1
        if bomb_g > 255: bomb_g = 1
        if bomb_b > 255: bomb_b = 1
        # 点滅する爆弾は目に悪いので動作確認をする時はコメントアウトする事
        pg.draw.circle(bomb_sfc, (bomb_r, bomb_g, bomb_b), (10, 10), 10) # 円の色を更新する


        txt = znk_sfc.render(f"koukaton * {zanki}", True, (0, 0, 0))
        scrn_sfc.blit(txt, (10, 10))

        
        scrn_sfc.blit(square_sfc, square_rct)

        if square_rct.colliderect(bomb_rct): # 障害物に爆弾が触れた時の処理
            vx *= -1
            vy *= -1

        if square_rct.colliderect(tori_rct): # 障害物にこうかとんが触れた時の処理
            if key_states[pg.K_LEFT]:tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:tori_rct.centerx -= 1
            if key_states[pg.K_UP]:tori_rct.centery += 1
            if key_states[pg.K_DOWN]:tori_rct.centery -= 1


        if tori_rct.colliderect(bomb_rct): # ゲームオーバー判定
            zanki -= 1
            vx *= -1
            vy *= -1
            tori_sfc = pg.image.load(choice(tori_img))
            tori_sfc = pg.transform.rotozoom(tori_sfc,0, 2.0)
            if zanki == 0:
                return
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()