import random
import keyboard as kb
import pyperclip as pc
from time import sleep


def single_temp() -> str:
    """ generate single random temperature """
    return '36.' + str(random.randint(1, 5))


def gen_three_temp() -> str:
    """ generate three temperatures"""
    res = ''
    for _ in range(3):
        res += single_temp() + '/'
    return res[:-1]


def callback() -> None:
    """ the callback function being hooked by hotkeys"""
    sleep(.1)
    temp = gen_three_temp()
    pc.copy(temp)
    print('已复制体温：{}'.format(temp))


if __name__ == '__main__':
    print('连续按下 Ctrl+V 可以无限生成体温')
    callback()
    kb.add_hotkey('ctrl+v', callback)
    kb.wait('esc')