import time
import yaml
import pyperclip as clip
import keyboard


def translate_into_flower(text, type=5):
    """
    ### 把文本处理成花体字

    - `text`: 输入的英文文本
    - `type`: 输出花体字的类型

    1. 𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔢
    2. 𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸
    3. 𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅
    4. 𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢
    5. 𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒
    6. 🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹
    7. ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚ
    8. 𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧
    9. a̶b̶c̶d̶e̶f̶g̶h̶i̶j̶k̶l̶m̶n̶o̶p̶q̶r̶
    """
    with open('flower.yml', 'r', encoding='utf-8') as f:
        dct = yaml.safe_load(f)
    original = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = ''.maketrans(original, dct[type])
    return text.translate(table)


def callback():
    """
    ### 只是一个简单的用来挂快捷键的函数
    """
    print('callback function envoked')
    time.sleep(0.5)
    keyboard.send('ctrl+a')
    time.sleep(0.1)
    keyboard.send('ctrl+c')
    ori = clip.paste()
    res = translate_into_flower(ori)
    print('原始', ori, '处理', res)
    clip.copy(res)
    keyboard.send('ctrl+v')
    keyboard.send('enter')


def listen_clipboard():
    hotkey = 'ctrl+shift'
    print(f'Listening clipboard... Press {hotkey} to execute')
    keyboard.add_hotkey(hotkey, callback)
    keyboard.wait()


if __name__ == '__main__':
    TEXT = 'this is a secret text, it is being processed by a mysterious function'
    MODE = 5
    res = translate_into_flower(TEXT, MODE)
    print(res)
    # listen_clipboard()