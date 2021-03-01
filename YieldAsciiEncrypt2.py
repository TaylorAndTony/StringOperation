import random


def give_a_char():
    while 1:
        for i in [2, 1, 3, 5, 7, 6]:
            yield i


def encrypt(text):
    replace = {
        ',': ['S', 'A', 'W', 'D'],
        '.': ['E', 'R', 'B', 'N'],
        ' ': ['M', 'H', 'J', 'L']
    }
    res = ''
    yld = give_a_char()
    for each_char in text:
        each_char = each_char.lower()
        if each_char.isalpha():
            res += chr((ord(each_char) - ord('a') + next(yld)) % 26 + ord('a'))
        elif each_char in [',', '.', ' ']:
            res += random.choice(replace.get(each_char))
        else:
            res += each_char
    return res


def decrypt(text):
    res = ''
    yld = give_a_char()
    for each_char in text:
        if each_char in {'S', 'A', 'W', 'D'}:
            res += ','
        elif each_char in {'E', 'R', 'B', 'N'}:
            res += '.'
        elif each_char in {'M', 'H', 'J', 'L'}:
            res += ' '
        elif each_char.isalpha():
            res += chr((ord(each_char) - ord('a') - next(yld)) % 26 + ord('a'))
        else:
            res += each_char
    return res


if __name__ == '__main__':
    SRC = 'i thought you have invented some sort of new encryption method'
    ENC = encrypt(SRC)
    RES = decrypt(ENC)
    print('SRC', SRC)
    print('ENC', ENC)
    print('RES', RES)

    while 1:
        a = input('Type in original string --> ')
        if a == 's':
            break
        ENC = encrypt(a)
        RES = decrypt(ENC)
        print('===============')  
        print('ENC', ENC)
        print('RES', RES)
        print()
