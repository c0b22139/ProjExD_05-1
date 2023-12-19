import os
import sys
import math
import pygame as pg
import random

WIDTH = 1600
HEIGHT = 900
MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]

class Card(pg.sprite.Sprite):
    '''
    カードに関するクラス
    '''
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
            },
        None:
            {
                None: "back@2x.png"
            }
        }
    
    used_card = {}
    def __init__(self, s: str, r: str, xy: tuple[int, int]):
        '''
        カード画像のSurfaceを生成する
        引数1 s: カードの絵柄
        引数2 r: カードの数字
        引数3 xy: カード画像の位置座標タプル
        '''
        super().__init__()
        self.r = r
        self.s = s
        self.image = pg.transform.rotozoom(pg.image.load(f'{MAIN_DIR}/playingcard-mini/{__class__.card[s][r]}'), 0, 1.5)
        self.rect = self.image.get_rect()
        self.rect.center = xy
    
    def number(self) -> int:
        '''
        カードの数字を返す関数
        戻り値 num: カードの数字
        '''
        if self.r == 'J' or self.r == 'Q' or self.r == 'K':
            num = 10
        elif self.r == 'A':
            num = 1
        return int(num)



def main():
    pg.display.set_caption('black jack')
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill((70, 128, 79))
    
    player_cards = pg.sprite.Group()
    dealer_cards = pg.sprite.Group()
    suits = ['h', 's', 'd', 'k']
    ranks = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    p_card_suits = [random.choice(suits) for i in range(2)]
    p_card_ranks = [random.choice(ranks) for i in range(2)]
    d_card_suits = [random.choice(suits) for i in range(2)]
    d_card_ranks = [random.choice(ranks) for i in range(2)]
    
    tmr = 0
    clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        for i in range(2):
            player_cards.add(Card(p_card_suits[i], p_card_ranks[i], (750+100*i, 900-225)))
        
        dealer_cards.add(Card(d_card_suits[0], d_card_ranks[0], (750+100*0, 225)))
        dealer_cards.add(Card(None, None, (750+100*1, 225)))
        #cards.update(screen)
        player_cards.draw(screen)
        dealer_cards.draw(screen)
        pg.display.update()
        tmr += 1
        clock.tick(50)
        
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()