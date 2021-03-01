import random


def bin_stars(text, choices=['*', '#', '^'], bg=' '):
    """
    把文本中每个字符的 ASCII 编码转换为二进制
    遇到 1 则随机打印 choices，否则打印 bg
    """
    res = ''
    for char in text:
        num = ord(char)
        # 1100001
        binarys = str(bin(num)[2:])
        # 01100001
        binarys = binarys.zfill(8)
        for binary in binarys:
            # 如果二进制数据是一
            if int(binary):
                c = random.choice(choices)
                res += c
            # 如果不是一
            else:
                res += bg
        res += '\n'
    print(res)
        # print(char, num, binarys, sep='\t')
    return res


def decrypt_bin_stars(text:str, choices:dict={'*', '#', '^'}):
    """
    解密由 bin_stars 加密的字符串
    :param text: 加密的字符串
    :param choices: 由 bin_stars 用于加密的随机内容
    """
    # lines: ['## *' ,  '#^  ^ ^']
    res = ''
    bin_code = ''
    bin_codes = []
    lines = text.splitlines()
    for single_letter in lines:
        # single_letter: '## *'
        for code in single_letter:
            # code: #
            if code in choices:
                bin_code += '1'
            else:
                bin_code += '0'
        bin_codes.append(bin_code)
        bin_code = ''
    # bin_codes: ['01101000', '01100101', '01101100',]
    for i in bin_codes:
        res += chr(int(i, 2))
    print(res)
    return res

def mess_code_encrypt(text):
    """
    把一串字符加密成 &#@*($&@#($%&))
    A           B           C            D
    65          66          67           68
    065         066         067          068
    )^%         )^^         )^&          )^*
    """
    mapping = {
        '0': ')',
        '1': '!',
        '2': '@',
        '3': '#',
        '4': '$',
        '5': '%',
        '6': '^',
        '7': '&',
        '8': '*',
        '9': '(',
    }
    result = ''
    for letter in text:
        # letter: str a
        ascii = str(ord(letter))
        ascii = ascii.zfill(3)
        # ascii: str 097
        for num in ascii:
            # num: str 0
            result += mapping.get(num)
    print(result)
    return result


def mess_code_decrypt(text):
    mapping = {
        ')': '0',
        '!': '1',
        '@': '2',
        '#': '3',
        '$': '4',
        '%': '5',
        '^': '6',
        '&': '7',
        '*': '8',
        '(': '9',
    }
    ascii = ''
    for code in text:
        ascii += mapping.get(code)
    # 每三个分隔到一个列表里
    chars = []
    for i in range(int(len(text) / 3)):
        secrets = text[i * 3:i * 3 + 3]
        temp = ''
        for secret in secrets:
            temp += mapping.get(secret)
        chars.append(temp)
    # chars: ['097', '119', '101',]
    result = ''
    for ascii_num in chars:
        ascii = int(ascii_num)
        result += chr(ascii)
    print(result)
    return result

if __name__ == '__main__':
    info = 'hello world'
    enc = bin_stars(info)
    decrypt_bin_stars(enc)
