import pyperclip as pc
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication

import etchedEmojiFunc


class UI:
    def __init__(self):
        self.app = QApplication([])
        self.window = QUiLoader().load('ui.ui')
        self.window.copy.clicked.connect(self.copyCon)
        self.window.paste.clicked.connect(self.pasteCon)
        self.window.clear.clicked.connect(self.clear)
        self.window.inEdit.textChanged.connect(self.callback_of_change)

    def clear(self):
        self.window.inEdit.clear()
        self.window.outEdit.clear()

    def pasteCon(self):
        self.window.inEdit.paste()

    def copyCon(self):
        text = self.window.outEdit.toPlainText()
        print(text)
        pc.copy(text)

    def callback_of_change(self):
        text = self.window.inEdit.text()
        if len(text) > 1:
            etched = etchedEmojiFunc.gen_anything(text)
            self.window.outEdit.setPlainText(etched)
        else:
            self.window.outEdit.setPlainText('长度不足')

    def run(self):
        self.window.show()
        self.app.exec_()


if __name__ == '__main__':
    ui = UI()
    ui.run()
