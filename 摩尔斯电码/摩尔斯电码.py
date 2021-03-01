from playsound import playsound
from time import sleep


CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

TRANS = dict(zip(CODE.values(), CODE.keys()))


def a2mo(text, sep=' / '):
    """
    文本转摩尔斯
    """
    global CODE
    CODE[' '] = sep
    result = []
    for letter in text:
        result.append(CODE.get(letter.upper(), '[?]'))
    return ' '.join(result)


def mo2a(mo):
    """
    摩尔斯解码文本
    """
    global TRANS
    result = []
    mo = mo.strip().split(' ')
    for code in mo:
        result.append(TRANS.get(code, '[?]'))
    return ' '.join(result)


def play_mo(mo, lag=0.1):
    """
    发出摩尔斯电码的声音
    """
    for code in mo:
        if code == '.':
            playsound('short.wav')
            sleep(lag)
        elif code == '-':
            playsound('long.wav')
            sleep(lag)
        else:
            sleep(lag * 3)


def interative_mode_mo2a():
    while True:
        a = input('--> ')
        print(TRANS.get(a, 'none'))
    

def smart_interative_mode():
    while True:
        a = input('--[smart]--> ')
        if a[0] in {'.', '-'}:
            print(mo2a(a))
        elif a[0].isalpha():
            print(a2mo(a.upper()))
        else:
            print('input cannot be resolved')

if __name__ == "__main__":
    smart_interative_mode()
