from pprint import pprint


def processTxt(filePath, return_plain_text=False):
    with open(filePath, 'r', encoding='utf') as f:
        lines = f.read().splitlines()
    # 去除空行
    lines = [i for i in lines if i != '']
    original = lines[::2]
    translated = lines[1::2]
    # 翻译后的结尾可能没有标点符号
    pro_translated = []
    for i in translated:
        if i[-1] not in {'.', ',', '，', '。'}:
            pro_translated.append(i + '。')
        else:
            pro_translated.append(i)
    # 分类返回
    if return_plain_text:
        return ''.join(original), ''.join(pro_translated)
    return original, pro_translated


if __name__ == '__main__':
    FILE_NAME = 'taobao.txt'
    PLAIN_TEXT = False

    ori, trans = processTxt(FILE_NAME, PLAIN_TEXT)
    pprint(trans)