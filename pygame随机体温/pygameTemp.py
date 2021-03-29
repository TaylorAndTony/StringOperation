import random
import sys
import time
import pygame
import keyboard as kb
import pyperclip as pc


class RandPos:
    """ give a random position """

    def __init__(self, step, begin_at: tuple):
        self.beginx = begin_at[0]
        self.beginy = begin_at[1]
        self.index = 0
        self.xlist = [-step for _ in range(100)] + [step for _ in range(100)]
        self.ylist = [-step for _ in range(100)] + [step for _ in range(100)]
        self.flush()

    def flush(self):
        random.shuffle(self.xlist)
        random.shuffle(self.ylist)

    def next(self):
        posx = self.beginx + self.xlist[self.index]
        posy = self.beginy + self.ylist[self.index]
        self.beginx, self.beginy = posx, posy
        if self.index == len(self.xlist) - 1:
            self.flush()
            self.index = 0
        else:
            self.index += 1
        return posx, posy


def single_temp() -> str:
    """ generate single random temperature """
    return '36.' + str(random.randint(1, 6))


def gen_three_temp_with_tab() -> str:
    """ 返回诸如26.2\t36.1\t36.2\t烟台的字符串 """
    res = []
    res.append(single_temp())
    if TEMP_COUNT > 6:
        raise ValueError('由于标准体温限制，只能生成做多 6 个')
    while len(res) != TEMP_COUNT:
        new = single_temp()
        if new != res[-1]:
            res.append(new)
    if USE_CITY:
        res.append('烟台')
    return '\t'.join(res)


def generate():
    temp = gen_three_temp_with_tab()
    pc.copy(temp)


def main():
    # keyboard
    kb.add_hotkey('ctrl+v', generate)
    # game
    pygame.init()
    pygame.display.set_caption('宽带随机体温')
    size = (536, 539)
    # screen
    screen = pygame.display.set_mode(size)
    screen.fill('#FFFFFF')
    # image
    img = pygame.image.load('temp.png')
    bg = pygame.image.load('bg.jpg')

    begin = (30, 100)
    pos = RandPos(3, begin)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(bg, (0, 0))
        screen.blit(img, pos.next())
        pygame.display.flip()
        time.sleep(1 / 25)


if __name__ == '__main__':
    USE_CITY = True
    TEMP_COUNT = 3
    main()
