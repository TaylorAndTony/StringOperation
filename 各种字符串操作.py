import random
import time


def add_str_in_each_char(in_str, target_str):
    """
    在一个字符串的每个字符之间插入另一个字符串
    :param in_str: 原始字符串
    :param target_str: 插入的字符串
    """
    in_str = in_str.replace('', target_str)
    return in_str[len(target_str):]


def dance(text):
    """
    让一个字符串在命令行蹦迪
    :param text: 待蹦迪的字符串
    """
    lst = list(text)
    while 1:
        random.shuffle(lst)
        temp = ' '.join(lst)
        print('\r%s' % temp, end='')
        time.sleep(0.1)


def add_hint(text: str, hint: str):
    """
    就是这个效果
    潜(wu)入(shuang)
    :param text: 潜入
    :param hint: wu shuang
    """
    hint = hint.split(' ')
    result = ''
    if len(text) == len(hint):
        bracket = ['(%s)' % i for i in hint]
        for original, modified in zip(text, bracket):
            result += original + modified
        return result
    else:
        return -1


if __name__ == '__main__':
    a = add_str_in_each_char('当猪飞的时候', '   ')
    print(a)
    b = add_hint('我明白了', '完 全 不 懂')
    print(b)
