import pyperclip as pc
import random


def gen_utf_char(num):
    """ generate a single UTF-8 char using its decimal code """
    code = 'u' + hex(num)[2:]
    temp = r"u'\{}'".format(code)
    return eval(temp)


def gen_continual_utf_char(a, b):
    """ generate all characters from a to b """
    res = ''
    for i in range(a, b):
        res += gen_utf_char(i)
    print(res)
    return res


def gen_random_utf_char(a, b, num):
    """ generate num times random characters from a to b """
    res = ''
    for _ in range(num):
        res += gen_utf_char(random.randint(a, b))
    print(res)
    return res


def make_punctuation(text):
    # 所有文本范围：[0, lenth]
    # 扷釐鄡欭檕庩嬄筡窌緛垣，嘵滊凧蔤錮，涼穱樓鞸。
    # <     group      >  <       >  <     >
    lenth = len(text)
    textList = list(text)
    insertPositions = []
    curID = 0
    # 找出应该加入标点符号的位置，这个 insertPosition 列表最后一个应该删掉。
    while curID < lenth:
        groupLenth = random.randint(5, 12)
        curID += groupLenth
        insertPositions.append(curID)
    # 开始插入
    for insertPos in insertPositions:
        textList.insert(insertPos, random.choice(['，', '，', '，', '。']))
    finalText = ''.join(textList) + '。'
    return finalText.replace('。', '。\n')


def mess_and_copy():
    s = ''
    for _ in range(10):
        s += gen_utf_char(random.randint(20000, 30000))
    print(s)
    pc.copy(s)


def mess():
    a = gen_random_utf_char(20000, 30000, 400)
    # pc.copy(a)
    b = make_punctuation(a)
    print(b)


def test():
    # 19904 19967
    for i in range(126976, 127019 + 1):
        print(gen_utf_char(i), end='')
    print()


def rand_less_strokes(times):
    """
    随机输出简单的汉字
    """
    s = ''
    with open('chars.txt', 'r', encoding='utf-8') as f:
        lst = list(f.read())
    for _ in range(times):
        s += random.choice(lst)
    pc.copy(s)
    print(s)


if __name__ == '__main__':
    # 中文： 19968-40865
    START = 19968
    END = 40865
    BEGIN = 20000
    GAP = 20
    rand_less_strokes(30)
