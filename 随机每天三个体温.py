import random
import pyperclip as clip
from win10toast import ToastNotifier


def raise_notification(headline, content):
    toaster = ToastNotifier()
    toaster.show_toast(headline, content, duration=2,
                       icon_path='F:/Icon/Icon8/temp.ico')


def gen_single_temp2():
    temp = random.uniform(36.0, 36.6)
    tar = '%.1f' % temp
    return tar


def gen_3_different_temp():
    result = []
    while len(result) != 3:
        cur = gen_single_temp2()
        if cur not in result:
            result.append(cur)
    return '/'.join(result)


def smart():
    result = gen_3_different_temp()
    print(result)
    clip.copy(result)
    raise_notification('随机体温生成器', f'体温 {result} 已复制\nヾ(≧▽≦*)o')
    print(f'结果 {result} 已复制')


if __name__ == "__main__":
    smart()
