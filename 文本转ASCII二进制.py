from os import system
from rich.console import Console


def word_to_ascii(text, sep='-'):
    """
    文本转 ASCII 码
    """
    result = []
    for each_word in text.strip():
        if each_word == ' ':
            result.append(sep)
        else:
            result.append(str(ord(each_word)))
            result.append(sep)
    return ''.join(result).rstrip(sep)


def ascii_to_word(ascii_string, sep='-'):
    """
    ASCII 码转文本
    """
    # 104-101-108-108-111--119-111-114-108-100
    word_separator = sep * 2
    words = ascii_string.split(word_separator)
    result = ''
    for word in words:
        # word: 104-101-108-108-111
        letters = word.split(sep)
        # letters: 104, 101, 108, 108, 111
        for letter in letters:
            # letter: 104
            result += chr(int(letter))
        result += ' '
    return result


def word_to_bin(text, sep='-'):
    """
    文本转二进制
    """
    result = ''
    for word in text:
        if word == ' ':
            result += sep
        else:
            ascii = ord(word)
            binary = bin(ascii)[2:]
            result += binary
            result += sep
    return result.rstrip(sep)


def bin_to_word(bin_string, sep='-'):
    """
    二进制转文本
    """
    word_separator = sep * 2
    words = bin_string.split(word_separator)
    result = ''
    for word in words:
        letters = word.split(sep)
        for letter in letters:
            result += chr(int(letter, 2))
        result += ' '
    return result


def smart_interactive_mode():
    console = Console()
    print()
    console.print('[yellow]tb[/yellow] : 文本转 ASCII 二进制编码')
    console.print('[yellow]ta[/yellow] : 文本转 ASCII 编码')
    console.print('[yellow]bt[/yellow] : ASCII 二进制编码转文本')
    console.print('[yellow]at[/yellow] : ASCII 编码转文本')
    print()
    while True:
        console.print('-- tb ta bt at --> ', style='bold cyan', end='')
        a = input()
        if a == 's' or a == '0':
            break
        elif len(a) <= 2:
            print('未知模式')
            continue
        mode, text = a[:2], a[3:]
        try:
            if mode == 'tb':
                print(word_to_bin(text))
            elif mode == 'bt':
                print(bin_to_word(text))
            elif mode == 'ta':
                print(word_to_ascii(text))
            elif mode == 'at':
                print(ascii_to_word(text))
            else:
                print('未知模式')
                continue
        except ValueError:
            print('数值有误')


if __name__ == "__main__":
    a = bin_to_word('01001010-01100001-01100011-01001111')
    print(a)
