from time import sleep
from threading import Thread

from playsound import playsound
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication


class UI:
    """ A GUI version of smart morse parser """
    def __init__(self):
        self.app = QApplication([])
        self.window = QUiLoader().load('morseUI.ui')
        self.window.inputCopy.clicked.connect(self.inputCopy)
        self.window.inputPaste.clicked.connect(self.inputPaste)
        self.window.inputClear.clicked.connect(self.inputClear)
        self.window.parseCopy.clicked.connect(self.parseCopy)
        self.window.parseClear.clicked.connect(self.parseClear)
        self.window.refresh.clicked.connect(self.refresh)
        self.window.playSound.clicked.connect(self.playSound)
        self.window.inputTextArea.textChanged.connect(self.handleTextChange)
        self.window.sepWordWithLine.stateChanged.connect(self.refresh)

    def block_play_sound(self, a, b):
        if a[0] in {'.', '-'}:
            play_mo(a)
        elif b[0] in {'.', '-'}:
            play_mo(b)
        else:
            print('没有找到摩尔斯电码符号')

    def playSound(self):
        ori = self.window.inputTextArea.toPlainText()
        out = self.window.outTextArea.toPlainText()
        t = Thread(target=self.block_play_sound, args=(ori, out,))
        t.setDaemon(True)
        t.start()

    def refresh(self):
        self.handleTextChange()

    def handleTextChange(self):
        original = self.window.inputTextArea.toPlainText()
        result = self.smart_decision(original)
        print(result)
        self.window.outTextArea.setPlainText(result)

    def inputCopy(self):
        self.window.inputTextArea.copy()

    def inputPaste(self):
        self.window.inputTextArea.paste()

    def inputClear(self):
        self.window.inputTextArea.clear()

    def parseCopy(self):
        self.window.outTextArea.copy()

    def parseClear(self):
        self.window.outTextArea.clear()

    def smart_decision(self, a):
        """ 智能决定输入的是字母还是摩尔斯，返回对应 """
        if a[0] in {'.', '-'}:
            return self.mo2a(a)
        elif a[0].isalpha():
            return self.a2mo(a.upper())
        else:
            return '[?]'

    def a2mo(self, text, sep=' / '):
        """
        文本转摩尔斯
        """
        global CODE
        if self.window.sepWordWithLine.isChecked():
            CODE[' '] = sep
        else:
            CODE[' '] = ''
        result = []
        for letter in text:
            result.append(CODE.get(letter.upper(), '[?]'))
        return ' '.join(result)

    def mo2a(self, mo):
        """
        摩尔斯解码文本
        """
        global TRANS
        result = []
        mo = mo.strip().split(' ')
        for code in mo:
            result.append(TRANS.get(code, '[?]'))
        return ' '.join(result)

    def run(self):
        """ let the application run """
        self.window.show()
        self.app.exec_()


CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}

TRANS = dict(zip(CODE.values(), CODE.keys()))


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


if __name__ == "__main__":
    ui = UI()
    ui.run()
