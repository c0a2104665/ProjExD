import pygame as pg
import sys
import random
import tkinter.messagebox as tkm

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろこうかとん") #タイトルバーに「←」を表示する
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()

    #背景
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    #clock.tick(0.5)

    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900,400
    #screen_sfc.blit(kkimg_sfc,kkimg_rct)

    #練習Ⅴ：爆弾
    bmimg_sfc = pg.Surface((20,20)) #Surface
    bmimg_sfc.set_colorkey((0,0,0)) 
    pg.draw.circle(bmimg_sfc,(255,0,0),(10,10),10)
    bmimg_rct = bmimg_sfc.get_rect()   #Rect
    bmimg_rct.centerx = random.randint(0,screen_rct.width)
    bmimg_rct.centery = random.randint(0,screen_rct.height)

    vx, vy = +1, +1 #練習Ⅵ

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True: kkimg_rct.centery -= 1#座標を-1
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery += 1#y座標を+1
        if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -= 1#x座標を-1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1#x座標を+1

        #練習Ⅶ
        if check_bound(kkimg_rct,screen_rct) != (1,1):
            if key_states[pg.K_UP] == True: kkimg_rct.centery += 1#座標を-1
            if key_states[pg.K_DOWN] == True: kkimg_rct.centery -= 1#y座標を+1
            if key_states[pg.K_LEFT] == True: kkimg_rct.centerx += 1#x座標を-1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 1#x座標を+1
        

        bmimg_rct.move_ip(vx,vy)
        

        screen_sfc.blit(bmimg_sfc,bmimg_rct)

        yoko, tate = check_bound(bmimg_rct,screen_rct)
        vx *= yoko
        vy *= tate

        #こうかとんが爆弾に３回ぶつかったら、処理を終了する
        count = []         #空リストを作成
        if kkimg_rct.colliderect(bmimg_rct):
            count.append("1") #文字をリスト追記
            print(count)
            if len(count) == 3:#リストの数が３になったら処理を終了する
                tkm.showwarning("ゲームオーバー")
                return
        

        print(count)  
                

        pg.display.update()
        clock.tick(1000)


def check_bound(rect,scr_rect):
    yoko, tate = +1, +1
    if rect.left < scr_rect.left or scr_rect.right < rect.right:yoko = -1
    if rect.top < scr_rect.top or scr_rect.bottom < rect.bottom:tate = -1
    return yoko,tate


if __name__ == "__main__":
    pg.init() #pygameを初期化
    main()    #main関数の呼び出し
    pg.quit() #pygameの初期化を解除する　initの逆
    sys.exit()#終了するはず


