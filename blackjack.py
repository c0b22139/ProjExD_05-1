import os
import sys
import math
import pygame as pg
import random

WIDTH = 1600
HEIGHT = 900
MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]


class Card():
    '''
    カードの情報を保存し、絵柄と数字を返すクラス
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
    suits = ['h', 's', 'd', 'k']

    ranks = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    used_card = {}
    def __init__(self, s: str, r: str):
        '''
        カード画像のSurfaceを生成する
        引数1 s: カードの絵柄
        引数2 r: カードの数字
        '''
        self.r = r
        self.s = s
    
    def __int__(self) -> int:
        '''
        カードの数字を返す関数
        戻り値 num: カードの数字
        '''
        if self.r == 'J' or self.r == 'Q' or self.r == 'K':
            num = 10
        elif self.r == 'A':
            num = 1
        else:
            num = int(self.r)
        return num
    
    def __str__(self):
        return self.s


class Deck():
    '''
    カードをシャッフルし、山札とするクラス
    このクラスを利用することで重複をなくす
    '''
    def __init__(self):
        self.cards = []
        for i in Card.suits:
            for j in Card.ranks:
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def draw(self) -> Card:
        '''
        シャッフルされたカードのリストから要素を取り出す関数
        戻り値: Cardクラスのインスタンス
        '''
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Image(pg.sprite.Sprite):
    '''
    カードのSurfaceを作成するクラス
    '''
    def __init__(self, s: str, r: int, xy: tuple[int, int]):
        '''
        引数1: カードの絵柄
        引数2: カードの数字
        '''
        super().__init__()
        self.s = s
        self.r = r
        self.image = pg.transform.rotozoom(pg.image.load(f'{MAIN_DIR}/playingcard-mini/{Card.card[s][r]}'), 0, 1.5)
        self.rect = self.image.get_rect()
        self.rect.center = xy


class Player():
    '''
    プレイヤーのトータルを保存し、バースト判定を行うクラス
    '''
    def __init__(self):
        self.total = 0
        self.ofer = False
        
    def match(self):
        '''
        トータルからバーストしていないか確認する関数
        '''
        if self.total == 21:
            return True
        
        elif self.total > 21:
            return True
        
        else:
            return False

'''
class Game():
    def __init__(self):
        self.deck = Deck()
        self.p = Player()
        self.d = Player()
        
    def draw_img(self, card, xy):
        Image(card, xy)
        
    def play_game(self):
        pc1 = self.deck.draw()
        dc1 = self.deck.draw()
        pc2 = self.deck.draw()
        dc2 = self.deck.draw()
        self.p.total += int(pc1) + int(pc2)
        self.d.total += int(dc1) + int(dc2)
        
'''
'''
class Button(pg.sprite.Sprite):
    def __init__(self, text, b_color: tuple[int, int, int], hw: tuple[int, int], xy: tuple[int, int]):
        super().__init__()
        
        self.text = text
        self.font = pg.font.Font(None, 50)
        
        self.b_color = b_color
        self.sf = pg.Surface(hw)
        self.xy = xy
        self.hw = hw
        
        self.button = pg.draw.rect(self.sf, self.b_color, self.hw)
        self.rect = self.sf.get_rect()
        self.f_color = (0, 0, 0)
        self.tx = self.font.render(self.text, 0, self.f_color)
        
        self.rect.center = self.xy
    def update(self):
        self.tx = self.font.render(self.text, 0, self.color)
        self.sf.blit(self.tx, self.rect)
'''


class Chip:
    """
    チップに関するクラス
    """
    def __init__(self, c: int):
        self.value = c      # 手持ちのチップの数
        self.bet = 0        # ベットするチップの数
        self.now_bet = 0    # ベットされたチップの数
        self.bet_flag = 0   # ベットしたかどうか
        self.font = pg.font.Font(None, 100)
        self.color = (128, 0, 0)
        self.image_v = self.font.render(f"Chip: {self.value}", 0, self.color)
        self.rect_v = self.image_v.get_rect()
        self.rect_v.center = 180, HEIGHT-50
        self.image_b = self.font.render(f"Bet?: {self.bet}", 0, self.color)
        self.rect_b = self.image_b.get_rect()
        self.rect_b.center = 130, 50
        self.image_nb = self.font.render(f"Bet: {self.now_bet}", 0, self.color)
        self.rect_nb = self.image_nb.get_rect()
        self.rect_nb.center = 110, 50

    def update(self, screen: pg.Surface):
        self.image_v = self.font.render(f"Chip: {self.value}", 0, self.color)
        screen.blit(self.image_v, self.rect_v)

        if self.bet_flag == 0:
            self.image_b = self.font.render(f"Bet?: {self.bet}", 0, self.color)
            screen.blit(self.image_b, self.rect_b)
        else:
            self.image_nb = self.font.render(f"Bet: {self.now_bet}", 0, self.color)
            screen.blit(self.image_nb, self.rect_nb)


def main():
    pg.display.set_caption('black jack')
    screen = pg.display.set_mode((WIDTH, HEIGHT))  
    pg.mouse.set_visible(True)  # マウスカーソル表示
    
    player_cards = pg.sprite.Group()  # プレイヤーのカードを保存するスプリットグループ
    dealer_cards = pg.sprite.Group()  # ディーラーのカードを保存するスプリットグループ
    #buttons = pg.sprite.Group()
    
    p = Player()
    d = Player()
    
    deck = Deck()
    p1 = deck.draw() 
    p2 = deck.draw()
    d1 = deck.draw()
    d2 = deck.draw()
    
    p.total += int(p1) + int(p2)
    d.total += int(d1) + int(d2)

    chip = Chip(200)
    
    print(p.total)
    tmr = 0
    clock = pg.time.Clock()

    while True:
        screen.fill((70, 128, 79))
        key_lst = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
            if chip.bet_flag == 0:  # チップ決定のためのキー操作
                if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                    if chip.bet < chip.value :
                        chip.bet += 1
                if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                    if chip.bet > 0:
                        chip.bet -= 1
                if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    chip.bet_flag = 1
                    chip.now_bet = chip.bet
                    chip.value -= chip.bet
                    chip.bet = 0
            
        player_cards.add(Image(str(p1), p1.r, (750, 900-225)))
        player_cards.add(Image(str(p2), p2.r, (850, 900-225)))
        dealer_cards.add(Image(str(d1), d1.r, (750, 225)))
        dealer_cards.add(Image(str(d2), d2.r, (750+100*1, 225)))
        player_cards.draw(screen)
        dealer_cards.draw(screen)
        
        #buttons.add(Button('hit', (255, 0, 0), (50, 50), (0, 0)))
        #buttons.update()
        chip.update(screen)
        pg.display.update()
        tmr += 1
        clock.tick(50)
        
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()