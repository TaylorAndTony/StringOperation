import random
import math


def gen_words(lenth) -> str:
    tar = ''
    lst = ['易', '简']
    for _ in range(lenth):
        tar += random.choice(lst)
    return tar


def gen_word_2(lenth) -> str:
    lst = ['易', '简']
    tar = ''
    for _ in range(lenth):
        random.shuffle(lst)
        tar += ''.join(lst)
    return tar


def chengFaBiao():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{i}*{j}={i*j}', end='')
        print()


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, ratio):
        return Vector(self.x * ratio, self.y * ratio)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)


class Waifu:
    def __init__(self, name):
        print(f'{name}：你在想桃子')


if __name__ == '__main__':
    # print(gen_word_2(50))
    pass
