import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm

class Screen: #初期画面
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
    
class Bird: #こうかとんを描画
    def __init__(self, image:str, size:float,xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy
        print(self.rct.center)
        
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        #print(self.rct.centerx,self.rct.centery)


        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)

class Bomb: #爆弾を描画
    def __init__(self,color,size,vxy,scr:Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size,size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy        # 練習6
        tori_mx = self.rct.centerx
        tori_my = self.rct.centery
        #print(self.rct.centerx,self.rct.centery)
        
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
 
    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        # 練習5
        self.blit(scr)
        move_bomb_x = self.rct.centerx
        move_bomb_y = self.rct.centery
        
class shot: #爆弾にぶつかる回数を設定
    def button_click():
        tkm.showwarning("３回衝突したので","ゲームオーバー") 
    torilife = 3  #ライフを作成
    def seigen(): #衝突した場合
        global move_bomb_x, move_bomb_y, tori_mx, tori_my,torilife,button_click
        if (move_bomb_x + 10 > tori_mx and move_bomb_x +10 < tori_mx) and\
            (move_bomb_y + 10 > tori_my and move_bomb_y + 10 < tori_my):
            if torilife > 0 : #torilifeが0以上の場合
                torilife = torilife -1
            elif torilife <= 0: #tirilifeが3~0の場合
                button_click()
                return
  
def main(): #爆弾とこうかとんの描画
    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)

    while True:
        scr.blit()
        
        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        kkt.update(scr)
        bkd.update(scr)
        if kkt.rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(1000)

# 練習7
def check_bound(rct, scr_rct): #壁を作成
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()