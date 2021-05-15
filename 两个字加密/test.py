
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



if __name__ == '__main__':
    info = 'https://www.bilibili.com/video/BV1eq4y177AK'
    enc = ascii_encode(info, '0' '1')
    print(enc)