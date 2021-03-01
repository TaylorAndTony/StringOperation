import random
import time
import atomPrint
import threading
import sys
from tkinter import *


class App:
    def __init__(self):

        self.root = Tk()
        self.root.title('Warning')
        self.root.configure(background=BG)
        self.root.geometry('800x300')
        self.frame = Frame()

        self.lable = Label(self.frame, text=TEXT, fg=FG, bg=BG, font=FONT)
        self.lable.pack()
        self.frame.pack(expand=True)

    def run(self):
        print('=========')
        time.sleep(LAG)
        print('--------')
        time.sleep(1)
        self.frame.mainloop()


def change_window_color():
    global BG
    global FG
    time.sleep(LAG + 0.5)
    while True:
        BG = '#000000'
        FG = '#ff0000'
        app.root['background'] = BG
        app.lable['bg'] = BG
        app.lable['fg'] = FG
        app.lable.update()
        time.sleep(1)
        BG = '#ff0000'
        FG = '#000000'
        app.root['background'] = BG
        app.lable['bg'] = BG
        app.lable['fg'] = FG
        app.lable.update()
        time.sleep(1)


def change_color():
    global COLOR
    choice = [WHITE, RED, YELLOW, GREEN, CYAN, PURPLE, PINK]
    while True:
        for each in choice:
            random.shuffle(choice)
            COLOR = each
            time.sleep(random.uniform(0.2, 1))


def master():
    while True:
        choosed = content[:]  # 先把列表复制一遍
        while choosed:
            text = random.choice(choosed)  # 选择一项
            atomPrint.custom_color_print(text, COLOR)  # 把它打印出来
            sys.stdout.flush()
            del choosed[choosed.index(text)]  # 把选择的一项从列表中删除，防止重复输出
            if COLOR == RED:
                gap = 0.02
            else:
                gap = random.uniform(0.05, 0.2)
            time.sleep(gap)


if __name__ == '__main__':
    # App配置
    TEXT = 'Hacked!'
    LAG = 5.0
    FONT = ('Arial', 60)
    BG = '#000000'
    FG = '#ff0000'
    # 文本颜色配置
    COLOR = [255, 255, 255]
    WHITE = [255, 255, 255]
    RED = [231, 76, 60]
    YELLOW = [241, 196, 15]
    GREEN = [46, 204, 113]
    CYAN = [26, 188, 156]
    PURPLE = [155, 89, 182]
    PINK = [255, 188, 155]
    content = ['\tstrhtml.encoding = \'utf-8\'',
               '\timg_path = str(data[0])',
               'for(int a = 1; a<= tar; a++){',
               '{',
               '}',
               'def out():',
               'def enemy():',
               '\tplayerLife = playerLife - enemyAtt',
               '#include <iostream>',
               'if(a*a + b*b == c*c){',
               'cout<<\'testing\'<<endl;',
               'import java.util.Random',
               'Random radGen = new Random();',
               'Scanner ys = new Scanner(System.in);',
               'double x0 = x0s.nextDouble();',
               'window.title(\'My Window\')',
               '\tstyle1 = ttk.Style()',
               'window.mainloop()',
               'style2.configure("AW.TLabel", foreground="white", background="#3de1ad", font=(\'Arial\', 18), width=5)',
               '\tl1 = ttk.Label(text="Test", style="BW.TLabel")',
               'java.util.Scanner s = new java.util.Scanner(System.in);',
               'style1.configure("BW.TLabel", foreground="black", font=(\'Arial\', 18))'
               ]
    # 改文本颜色
    t = threading.Thread(target=change_color)
    t.setDaemon(True)
    t.start()

    app = App()

    # 主输出
    t = threading.Thread(target=master)
    t.setDaemon(True)
    t.start()
    # 改窗口颜色
    t = threading.Thread(target=change_window_color)
    t.setDaemon(True)
    t.start()

    app.run()