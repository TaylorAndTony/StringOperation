import random
from time import sleep
from tkinter import *

import keyboard as kb
import pyperclip as pc


class App:
    """ Super awesome temperature generator """

    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x140')
        self.root['background'] = '#000000'
        self.root.title('超级一键体温生成器')
        self.text = StringVar()
        self.label = Label(
            self.root,
            textvariable=self.text,
            font=('微软雅黑', 30),
            bg='#000000'
        )
        # 乱码
        self.mess_code = StringVar()
        self.mess_label = Label(
            self.root,
            textvariable=self.mess_code,
            font=('微软雅黑', 14),
            fg='#ffffff',
            bg='#000000'
        )
        with open('bin.txt', 'r', encoding='utf-8') as f:
            self.mess = f.read().replace('\n', '').replace(' ', '')

    def set_gui_effects(self):
        """ change some effects of this program """
        # change color
        c = random_color()
        self.label['fg'] = c
        self.label.update()
        # change font
        # f = random_font()
        # self.label['font'] = f
        # self.label.update()
        # loop call
        self.root.after(100, self.set_gui_effects)

    def quickly_effects(self):
        """ change the messcode effects """
        # char
        mess = self.mess
        messed = list(mess)
        random.shuffle(messed)
        self.mess_code.set(''.join(messed[:30]))
        self.mess_label['text'] = random.choice(mess)
        self.mess_label.update()
        self.root.after(30, self.quickly_effects)

    def layout(self):
        """ layout the app """
        self.mess_label.pack(padx=20, pady=10)
        self.label.pack(padx=20, pady=10)

    def generate(self):
        """ generate ready-to-use temperature """
        temp = gen_three_temp()
        pc.copy(temp)
        self.text.set(temp)

    def run(self):
        """ start the program """
        kb.add_hotkey('ctrl+v', self.generate)
        self.root.after(20, self.set_gui_effects)
        self.root.after(20, self.quickly_effects)
        self.generate()
        self.layout()
        self.root.mainloop()


def random_color():
    """ return a random color """
    colors = [
        '#f5222d',
        '#ff7a45',
        '#ffa940',
        '#ffc53d',
        '#ffec3d',
        '#bae637',
        '#73d13d',
        '#36cfc9',
        '#40a9ff',
        '#2f54eb',
        '#722ed1',
        '#eb2f96',
    ]
    return random.choice(colors)


def random_font():
    """ return a random font for tk program """
    f = [
        ('微软雅黑', 30),
        ('宋体', 30),
        ('黑体', 30),
        ('Arial', 30),
        ('仿宋', 30),
        ('Castellar', 30),
    ]
    return random.choice(f)


def single_temp() -> str:
    """ generate single random temperature """
    return '36.' + str(random.randint(1, 6))


def gen_three_temp() -> str:
    """ generate three temperatures"""
    res = ''
    for _ in range(3):
        res += single_temp() + '/'
    return res[:-1]


if __name__ == '__main__':
    app = App()
    app.run()
