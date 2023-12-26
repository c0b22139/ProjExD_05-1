import os
import sys
import math
import random
import pygame as pg
from pygame.sprite import AbstractGroup

WIDTH = 1600
HEIGHT = 900
MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]

class Card:
    card = {
        "h":
            {
                "A": 'h01@2x.png',
                "2": 'h02@2x.png',
                "3": 'h03@2x.png',
                "4": 'h04@2x.png',
                "5": 'h05@2x.png',
                "6": 'h06@2x.png',
                "7": 'h07@2x.png',
                "8": 'h08@2x.png',
                "9": 'h09@2x.png',
                "10": 'h10@2x.png',
                "J": 'h11@2x.png',
                "Q": 'h12@2x.png',
                "K": 'h13@2x.png'
            },
        "s":
            {
                "A": 's01@2x.png',
                "2": 's02@2x.png',
                "3": 's03@2x.png',
                "4": 's04@2x.png',
                "5": 's05@2x.png',
                "6": 's06@2x.png',
                "7": 's07@2x.png',
                "8": 's08@2x.png',
                "9": 's09@2x.png',
                "10": 's10@2x.png',
                "J": 's11@2x.png',
                "Q": 's12@2x.png',
                "K": 's13@2x.png'
            },
        "d":
            {
                "A": 'd01@2x.png',
                "2": 'd02@2x.png',
                "3": 'd03@2x.png',
                "4": 'd04@2x.png',
                "5": 'd05@2x.png',
                "6": 'd06@2x.png',
                "7": 'd07@2x.png',
                "8": 'd08@2x.png',
                "9": 'd09@2x.png',
                "10": 'd10@2x.png',
                "J": 'd11@2x.png',
                "Q": 'd12@2x.png',
                "K": 'd13@2x.png'
            },
        "k":
            {
                "A": 'k01@2x.png',
                "2": 'k02@2x.png',
                "3": 'k03@2x.png',
                "4": 'k04@2x.png',
                "5": 'k05@2x.png',
                "6": 'k06@2x.png',
                "7": 'k07@2x.png',
                "8": 'k08@2x.png',
                "9": 'k09@2x.png',
                "10": 'k10@2x.png',
                "J": 'k11@2x.png',
                "Q": 'k12@2x.png',
                "K": 'k13@2x.png'
            }
        }
    
    def __init__(self, s, r):
        self.r = r
        self.s = s
        self.img = pg.transform.rotozoom(pg.image.load(f'{MAIN_DIR}/playingcard-mini/{__class__.card[s][r]}'), 0, 2.0)
        self.rct = self.img.get_rect()
        self.rct.center = (800, 450)
        
    def update(self, screen: pg.Surface):
        screen.blit(self.img, self.rct)
        

class Hit(pg.sprite.Sprite):
    """
    ヒットに関するクラス
    """
    def __init__(self, card: Card, hit_num):
        """
        新たにトランプを一枚引く
        引数1 card：持ち札のカード
        引数2 hit_num：ヒットした回数
        """
        super().__init__()
        gara = ["h", "s", "d", "k"]
        num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.img = pg.transform.rotozoom(pg.image.load(f'{MAIN_DIR}/playingcard-mini/{Card.card[random.choice(gara)][random.choice(num)]}'), 0, 2.0)
        self.rct = self.img.get_rect()
        self.rct.centerx = card.rct.centerx + 20*hit_num
        self.rct.centery = card.rct.centery + 20*hit_num

    def update(self, screen: pg.Surface):
        screen.blit(self.img, self.rct)


class Stand(pg.sprite.Sprite):
    """
    スタンドに関するクラス
    """
    def __init__(self, life: int):
        # スタンドと表示する
        super().__init__()
        self.font = pg.font.Font(None, 50)
        self.color = (255, 0, 0)
        self.image = self.font.render(f"Stand", 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH/2, HEIGHT/2
        self.life = life

    def update(self, screen: pg.Surface):
        self.image = self.font.render(f"Stand", 0, self.color)
        screen.blit(self.image, self.rect)
        self.life -= 1
        if self.life < 0:
            self.kill()

    

def main():
    pg.display.set_caption('black jack')
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    # 背景
    card = Card("d",'A')
    hit = pg.sprite.Group()
    stand = pg.sprite.Group()
    clock = pg.time.Clock()
    tmr = 0
    hit_num = 0  # プレイヤーがそのラウンドでヒットした回数
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
            # h押下でヒット
            if event.type == pg.KEYDOWN and event.key == pg.K_h:
                hit_num += 1
                hit.add(Hit(card, hit_num))
            
            # s押下でスタンド
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                hit_num = 0  # ヒット回数のリセット
                stand.add(Stand(60))
            
        card.update(screen)
        hit.update(screen)
        stand.update(screen)
        pg.display.update()
        tmr += 1
        clock.tick(50)
        
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()