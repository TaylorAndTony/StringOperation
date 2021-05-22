"""
Use two chinese characters and just one english character
to encode and decode a UTF-8 or ASCII string
"""
import base64 as b64


def green_print(content):
    print(f'\033[32m{content}\033[0m')


def ascii_encode(text, zero, one, sep='-') -> str:
    """
    First encode the text using ASCII
    then convert the ASCII to binary
    and replace 0 with zero, 1 with one
    :param text: the text wait to be encoded
    :param zero: 0 is replaces by this
    :param one: 1 is replaces by this
    :param sep: which char separates the test
    """
    asciis = [ord(i) for i in text]
    bins = [str(bin(i))[2:] for i in asciis]
    res = ''
    for b in bins:
        # b: 1110111
        for char in b:
            # char: 1 or 0
            if char == '1':
                res += one
            else:
                res += zero
        res += sep
    return res[:-1]


def ascii_decode(text, zero, sep='-'):
    """
    Decode a text that is encoded with function ascii_encode()
    Since there are only two characters encoding the msg,
    you only need to tell which one is stands for zero,
    as the other must be the one.
    :param text: the text
    :param zero: replace this to 0
    :param sep: which char separates the test
    """
    group = text.split(sep)
    bins_arr = []
    this = ''
    for g in group:
        for char in g:
            if char == zero:
                this += '0'
            else:
                this += '1'
        bins_arr.append(this)
        this = ''

    res = ''
    for bins in bins_arr:
        num = int(bins, 2)
        res += chr(num)
    return res


def b64_encode(text, zero, one, sep='-'):
    msg = b64.b64encode(text.encode('utf-8')).decode('utf-8')
    return ascii_encode(msg, zero, one, sep)


def b64_decode(text, zero, sep='-'):
    temp = ascii_decode(text, zero, sep)
    return b64.b64decode(temp.encode('utf-8')).decode('utf-8')


def ascii_aio(text, zero, one, sep='-'):
    enc = ascii_encode(text, zero, one, sep)
    green_print('加密后:')
    print(enc)
    dec = ascii_decode(enc, zero, sep)
    green_print('解密后:')
    print(dec)


def b64_aio(text, zero, one, sep='-'):
    enc = b64_encode(text, zero, one, sep)
    green_print('加密后:')
    print(enc)
    dec = b64_decode(enc, zero, sep)
    green_print('解密后:')
    print(dec)


if __name__ == '__main__':
    info = 'https://www.bilibili.com/'
    ascii_aio(info, '嗷', '唔', '~')
