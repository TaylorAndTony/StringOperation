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
        self.x = random.randint(130, 200)
        self.y = random.randint(50, 100)
        # change temp
        self.text = self.canvas.create_text(
            self.x, self.y, text=self.tiwen, font=('微软雅黑', 16))
        self.root.after(60, self.animate)

    def generate(self):
        """ generate ready-to-use temperature """
        temp = gen_three_temp_with_tab()
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

def gen_three_temp_with_tab() -> str:
    """ 返回诸如26.2\t36.1\t36.2\t烟台的字符串 """
    res = []
    res.append(single_temp())
    while len(res) != 3:
        new = single_temp()
        if new != res[-1]:
            res.append(new)
    res.append('烟台')
    return '\t'.join(res)


if __name__ == '__main__':
    app = App()
    app.run()
