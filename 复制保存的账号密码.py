import random

map = {
        '0': '@',
        '1': '%',
        '2': '^',
        '3': '!',
        '4': '<',
        '5': '-',
        '6': '+',
        '7': '*',
        '8': '?',
        '9': '&',
    }
# mi = dict(zip(m.values(), m.keys()))
reversed_map = dict(zip(map.values(), map.keys()))

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


def process_number(nums: str, mode='enc'):
    if mode == 'enc':
        result = ''
        for num in nums:
            result += map.get(num, num)
        return result
    elif mode == 'dec':
        result = ''
        for num in nums:
            result += reversed_map.get(num, num)
        return result
    else:
        return -1


def smart_process(text, mode='+'):
    if mode == '+':
        return encrypt(process_number(text, 'enc'))
    elif mode == '-':
        return decrypt(process_number(text, 'dec'))
    else:
        return -1


if __name__ == '__main__':
    USER = '%?-+%^^-*%@'
    PASS = '^?-+@--!!&nko'
    print(smart_process(PASS, '-'))