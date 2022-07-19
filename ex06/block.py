import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image

# 背景画像サイズ変更
moto_img = Image.open("data/mash.jpg")            
ch_img = moto_img.resize((910,1000),Image.BILINEAR)
ch_img.save("data/ch_mash.jpg")

# 描画する”Board”サイズ変更9
moto_png = Image.open("data/red_board.png")
ch_png = moto_png.resize((70,10),Image.BILINEAR)
ch_png.save("data/ch_red_board.png")


class Window: #初期画面
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
    
class Board: # 板の描画
    def __init__(self, image:str, size:float,xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy
        print(self.rct.center)
    
    def blit(self, scr:Window):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr: Window):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        
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

class Ball: # Ballの描画
    def __init__(self,color,size,vxy,scr:Window):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size,size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy        
        
    def blit(self,scr:Window):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr: Window):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        self.blit(scr)
        
def main(): #Board,ballを描画
    clock = pg.time.Clock()
    scr = Window("ブロック崩し", (910, 1000), "data/ch_mash.jpg")
    kkt = Board("data/ch_red_board.png", 2.0, (400, 980))
    bkd = Ball((255,255,255), 10, (+1,+1), scr)

    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        kkt.update(scr)
        bkd.update(scr)
        if kkt.rct.colliderect(bkd.rct):
            return
        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct): #壁を作成
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()