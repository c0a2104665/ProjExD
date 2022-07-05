import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろこうかとん") #タイトルバーに「←」を表示する
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("fig/bg.png")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    clock.tick(0.5)

    kkimg_sfc = pg.image.load("fig/bg.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900,400


    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:return
        
        pg.display.update()
        clock.tick(1000)
        

if __name__ == "__main__":
    pg.init() #pygameを初期化
    main()    #main関数の呼び出し
    pg.quit() #pygameの初期化を解除する　initの逆
    sys.exit()#終了するはず


