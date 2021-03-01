import random
import time
import pyperclip
import keyboard


def read_txt():
    lst = []
    with open('./content.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            lst.append(i.strip())
    return lst


def master():
    lst = read_txt()
    one = random.choice(lst)
    print('当前复制：', one)
    pyperclip.copy(one)


def send_msg(text):
    pyperclip.copy(text)
    keyboard.send('ctrl+v')
    keyboard.send('enter')
    time.sleep(0.2)


def bomber(times):

    def _gen():
        lst = read_txt()
        while True:
            random.shuffle(lst)
            for i in lst:
                yield i

    gen = _gen()
    print(f'即将输出 {times} 条文本，点击 QQ 聊天窗口并按下 shift')
    time.sleep(0.5)
    keyboard.wait('shift')
    for i in range(times):
        print(f'\rProgress: {i + 1} / {times}', end='')
        send_msg(next(gen))
    print()


if __name__ == "__main__":
    master()
    bomber(5)
