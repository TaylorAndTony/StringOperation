import yaml
from tkinter import *


class APP:
    def __init__(self):
        # text
        with open('flower.yml', 'r', encoding='utf-8') as f:
            self.dct = yaml.safe_load(f)
        self.root = Tk()
        self.root.wm_title('花体字生成')
        self.root.attributes('-topmost', 1)
        self.font = ('微软雅黑', 16)
        self.lay = {'padx': 10, 'pady': 5}
        # input
        self.input_var = StringVar()
        self.input_area = Entry(self.root,
                                font=self.font,
                                width=30,
                                textvariable=self.input_var)
        # output
        self.output_area = Text(self.root,
                                font=('微软雅黑', 20),
                                width=40,
                                height=12)

    def __get_input(self) -> str:
        return self.input_var.get()

    def __set_out(self, text):
        self.output_area.delete('1.0', "end")
        self.output_area.insert('0.0', text)

    def __callback(self):
        # 用户输入
        t = self.__get_input()
        # 转换表
        original = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        for typee in range(1, 9):
            print('============')
            print('ord:', typee)
            print('ori:', len(original))
            print('dct:', len(self.dct[typee]))
            table = ''.maketrans(original, self.dct[typee])
            result += t.translate(table) + '\n'
        self.__set_out(result)

    def layout(self):
        # input
        Label(self.root,
              text='输入：',
              font=self.font
              ).grid(row=0, column=0, **self.lay)
        self.input_area.grid(row=0, column=1, **self.lay)
        # button
        Button(self.root,
               text='刷新',
               font=self.font,
               command=self.__callback).grid(row=1, column=0, columnspan=2, **self.lay)
        # output
        self.output_area.grid(row=2, column=0, columnspan=2, **self.lay)

    def run(self):
        self.layout()
        self.root.mainloop()


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


if __name__ == '__main__':
    APP().run()
