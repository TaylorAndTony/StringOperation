import string
import os
from rich.console import Console
import atomPrint


def kaisa(s, k):
    lower = string.ascii_lowercase  # 小写字母
    upper = string.ascii_uppercase  # 大写字母
    before = string.ascii_letters  # 无偏移的字母顺序 小写+大写
    # 偏移后的字母顺序 还是小写+大写
    # 分别把小写字母和大写字母偏移后再加到一起
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = ''.maketrans(before, after)  # 创建映射表
    return s.translate(table)  # 对s进行偏移 即加密


def decrypt_kaisa(s):
    # 找出现概率最大的字母
    dct = {}
    for i in s:
        if i == ' ':
            continue
        dct[i] = dct.get(i, 0) + 1
    ordered = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    
    # 判断找到了多少个
    if len(ordered) > 4:
        # 找到 4 个出现次数最高的字母
        keys =  (ordered[0][0], ordered[1][0], ordered[2][0], ordered[3][0])
        # 整洁输出
        print('=' * len(s) + '\n')
        # 对于加密的字符串中的每一个
        print(f'原始文本：{s}\n')
        # 分类别输出
        # 第一个彩色打印
        key = ord(keys[0]) - ord('e')
        guessed_key = f'猜测密钥：{key}, '
        guessed_result = f'{kaisa(s, -key)}\n'
        console.print(guessed_key, 
                        style='bold yellow', 
                        end='')
        console.print('[bold yellow]解密结果：[/bold yellow]', 
                        guessed_result, 
                        style='bold cyan')
        # 剩下三个
        for each_letter in keys[1:]:
            # 找密钥
            key = ord(each_letter) - ord('e')
            print(f'猜测密钥：{key}, 解密结果：{kaisa(s, -key)}\n')
    
    else:
        print('数据量不足，结果可能有误')
        # 直接找第一个
        letter = ordered[0][0]
        # 找密钥
        key = ord(letter) - ord('e')
        print(f'▶猜测密钥：{key}, 解密结果：{kaisa(s, -key)}\n')


if __name__ == "__main__":
    console = Console()
    while 1:
        os.system('cls')
        a = input('输入待破解文本 --> ')
        if a == 's':
            break
        else:
            decrypt_kaisa(a)
        input('回车继续...')
