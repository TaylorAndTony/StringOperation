def give_a_char():
    while 1:
        for i in [2, 1, 3, 5, 7, 6]:
            yield i


def encrypt(text):
    res = ''
    yld = give_a_char()
    for each_char in text:
        each_char = each_char.lower()
        if each_char.isalpha():
            res += chr((ord(each_char) - ord('a') + next(yld)) % 26 + ord('a'))
        else:
            res += each_char
    return res


def decrypt(text):
    res = ''
    yld = give_a_char()
    for each_char in text:
        if each_char.isalpha():
            res += chr((ord(each_char) - ord('a') - next(yld)) % 26 + ord('a'))
        else:
            res += each_char
    return res


if __name__ == '__main__':
    SRC = 'hello world dfnidWW, 5+8-5'
    ENC = encrypt(SRC)
    RES = decrypt(ENC)
    print(SRC)
    print(ENC)
    print(RES)