import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろこうかとん") #タイトルバーに「←」を表示する
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("fig/bg.png")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    clock.tick(0.5)

    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900,400

    #練習Ⅴ：爆弾
    bmimg_sfc = pg.Surface((20,20)) #Surface
    bmimg_sfc.set_colorkry((0,0,0)) 
    pg.draw.circle(bmimg_sfc,(255,0,0),(10,10),10)
    bmimg_rct = bmimg_sfc.get_rect()   #Rect
    bmimg_rct.centery = random.randint(0,screen_rct.width)
    bmimg_rct.centery = random.randint(0,screen_rct.height)


    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:return
        
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True: kkimg_rct.centery -= 1#座標を-1
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery += 1#y座標を+1
        if key_states[pg.K_LEFT] == True: kkimg_rct.centery -= 1#x座標を-1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centery += 1#x座標を+1
        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        screen_sfc.blit(bmimg_sfc,bmimg_rct)

        pg.display.update()
        clock.tick(1000)
        

if __name__ == "__main__":
    pg.init() #pygameを初期化
    main()    #main関数の呼び出し
    pg.quit() #pygameの初期化を解除する　initの逆
    sys.exit()#終了するはず


