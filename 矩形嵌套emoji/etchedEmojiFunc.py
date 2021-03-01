from pprint import pprint, pp
from emoji import emojize
from pyperclip import copy
"""
000 0 000  0  |
011 1 110  1  |--> len(lst)
012 2 210  2  |
--------
  rows


1 / 4
[1, 2, 3, 4, 5, 6, 7, 8]
            i
000000000   0        7 + 2个 列表当前位置
011111111   1        6 + 2个 列表当前位置
012222222   2        5 + 2个 列表当前位置
012333333   3        4 + 2个 列表当前位置
012344444   4        3 + 2个 列表当前位置
012345555   5        2 + 2个 列表当前位置
012345666   6        1 + 2个 列表当前位置
012345677   7        0 + 2个 列表当前位置
"""


def gen_etched_rectangle(lst, center_element) -> list:
    lenth = len(lst)
    quard_text = []
    # 先把 1/4 前面的打完
    for line_id in range(lenth):
        plus_num = lenth - line_id + 2
        foregoing_part = ''.join([i for i in lst[:line_id]])
        latter_part = lst[line_id] * (plus_num - 2)
        quard_text.append(foregoing_part + latter_part)
    # pp(quard_text)
    # 每行后面缺一个当前行的最后一个字母
    quard_text_backup = quard_text[:]
    for line_id in range(lenth):
        quard_text[line_id] += quard_text[line_id][-1]
    quard_text_backup_reversed = []
    # 把缺少子母的前 1/4 反转
    for i in quard_text_backup:
        quard_text_backup_reversed.append(i[::-1])
    half_text = []
    # 然后合并两部分，下面的 half_text 是整个矩阵去除中间行的上半部分
    for a, b in zip(quard_text, quard_text_backup_reversed):
        half_text.append(a + b)
    # 生成中间行, 01234 3210
    center = ''.join(lst) + center_element + ''.join(lst[-1::-1])
    half_text_backup = half_text[:]
    half_text.append(center)
    for k in half_text_backup[::-1]:
        half_text.append(k)
    return '\n'.join(half_text)


def replace_items(text:str, ori:list, to:list) -> str:
    for i, j in zip(ori, to):
        text = text.replace(i, j)
    return text


def gen_complex_rectangle(strr):
    lst = list(strr)
    fake_pre = [str(i) for i in range(len(lst) - 1)]
    fake_last = '.'
    depature = fake_pre[:]
    depature.append(fake_last)
    res = gen_etched_rectangle(fake_pre, fake_last)
    print('replace {} -> {}'.format(depature, lst))
    rplc = replace_items(res, depature, lst)
    copy(rplc)
    print('结果已经复制')
    return rplc


def gen_etched_emoji(emojis):
    processed = []
    for i in emojis:
        processed.append(emojize(i))
    a = gen_complex_rectangle(processed)
    return a


def gen_anything(strr):
    lst = list(strr)
    a = gen_etched_rectangle(lst[:-1], lst[-1])
    return a


if __name__ == '__main__':
    # 😀😶😂😶😎🌏🌎🌋🗻🧭♨☎📱
    emojis = '📱😶📱'
    gen_anything(emojis)