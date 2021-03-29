import string
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
import pyperclip as pc


class UI:
    def __init__(self):
        self.app = QApplication([])
        self.window = QUiLoader().load('ui.ui')
        # buttons
        self.window.paste.clicked.connect(self.paste)
        self.window.clear.clicked.connect(self.clear)
        self.window.reverse.clicked.connect(self.reverse)
        self.window.copy.clicked.connect(self.copy)
        self.window.reverseKey.clicked.connect(self.reverseKey)
        self.window.plus.clicked.connect(self.plus)
        self.window.minus.clicked.connect(self.minus)
        # auto refresh args
        self.window.inText.textChanged.connect(self.inTextChange)
        # button refresh args
        self.window.refresh.clicked.connect(self.inTextChange)
        self.window.plus.clicked.connect(self.inTextChange)
        self.window.minus.clicked.connect(self.inTextChange)

    def paste(self):
        self.window.inText.paste()

    def clear(self):
        self.window.inText.clear()
        self.window.outText.clear()

    def reverse(self):
        src = self.window.inText.toPlainText()
        dst = self.window.outText.toPlainText()
        self.window.inText.setPlainText(dst)
        self.window.outText.setPlainText(src)

    def copy(self):
        a = self.window.outText.toPlainText()
        pc.copy(a)

    def getKey(self) -> int:
        txt = self.window.keyLine.text()
        if txt == '':
            txt = '0'
        return int(txt)

    def setkey(self, key: int):
        self.window.keyLine.setText(str(key))

    def reverseKey(self):
        self.setkey(-self.getKey())

    def plus(self):
        self.setkey(self.getKey() + 1)

    def minus(self):
        self.setkey(self.getKey() - 1)

    def inTextChange(self):
        src = self.window.inText.toPlainText()
        if len(src) > 0:
            # auto mode
            if self.window.rAuto.isChecked():
                decrypt = decrypt_kaisa(src)
                self.window.outText.setPlainText(decrypt)
            # enumerate mode
            elif self.window.rForce.isChecked():
                res = enumerate_decrypt(src)
                self.window.outText.setPlainText(res)
            # manual mode
            else:
                key = self.getKey()
                res = kaisa(src, key)
                self.window.outText.setPlainText(res)

    def run(self):
        self.window.show()
        self.app.exec_()


def kaisa(s, k) -> str:
    lower = string.ascii_lowercase  # 小写字母
    upper = string.ascii_uppercase  # 大写字母
    before = string.ascii_letters  # 无偏移的字母顺序 小写+大写
    # 偏移后的字母顺序 还是小写+大写
    # 分别把小写字母和大写字母偏移后再加到一起
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = ''.maketrans(before, after)  # 创建映射表
    return s.translate(table)  # 对s进行偏移 即加密


def decrypt_kaisa(s) -> str:
    # 找出现概率最大的字母
    dct = {}
    for i in s:
        if i == ' ':
            continue
        dct[i] = dct.get(i, 0) + 1
    ordered = sorted(dct.items(), key=lambda x: x[1], reverse=True)

    # 判断找到了多少个
    if len(ordered) > 4:
        # 找到 5 个出现次数最高的字母
        keys = (ordered[0][0], ordered[1][0], ordered[2][0], ordered[3][0],
                ordered[4][0])
        # 整洁输出
        # 对于加密的字符串中的每一个
        resultList = []
        for each_letter in keys:
            # 找密钥
            key = ord(each_letter) - ord('e')
            resultList.append(f'[{key}] ' + kaisa(s, -key))
        return '\n\n'.join(resultList)

    else:
        # 直接找第一个
        letter = ordered[0][0]
        # 找密钥
        key = ord(letter) - ord('e')
        return f'[{key}] ' + kaisa(s, -key) + ' [not sure]'


def enumerate_decrypt(s):
    res = []
    for i in range(1, 27):
        dec = kaisa(s, -i)
        res.append(f'[{i}] {dec}')
    return '\n'.join(res)


if __name__ == '__main__':
    ui = UI()
    ui.run()