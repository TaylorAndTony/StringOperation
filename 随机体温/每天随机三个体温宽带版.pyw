import random
from time import sleep
from tkinter import *

import keyboard as kb
import pyperclip as pc


class App:
    """ Super awesome temperature generator """

    def __init__(self):
        self.tiwen = '0/0/0'
        self.width = 400
        self.height = 140
        self.x = 200
        self.y = 70
        self.bg = '#ffffff'
        self.fg = '#ff0000'
        # GUI
        self.root = Tk()
        self.root.geometry('400x140')
        self.root['background'] = self.bg
        self.root.title('超级一键体温生成器')
        # canwas
        self.canvas = Canvas(self.root, width=self.width,
                             height=self.height, background=self.bg)
        self.text = self.canvas.create_text(self.x, self.y, text=self.tiwen)

    def layout(self):
        self.canvas.pack()

    def animate(self):
        # delete previous
        self.canvas.delete(self.text)
        # random positon
        if self.x > self.width or self.y > self.height:
            self.x += -20
            self.y += -20
        elif self.x < 0 or self.y < 0:
            self.x += 20
            self.y += 20
        else:
            self.x += random.randint(-15, 15)
            self.y += random.randint(-15, 15)
        # change temp
        self.text = self.canvas.create_text(
            self.x, self.y, text=self.tiwen, font=('微软雅黑', 24))
        self.root.after(50, self.animate)

    def generate(self):
        """ generate ready-to-use temperature """
        temp = gen_three_temp()
        pc.copy(temp)
        self.tiwen = temp

    def run(self):
        """ start the program """
        kb.add_hotkey('ctrl+v', self.generate)
        self.root.after(20, self.animate)
        self.layout()
        self.generate()
        self.root.mainloop()


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
