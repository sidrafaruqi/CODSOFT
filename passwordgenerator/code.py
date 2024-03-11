import random
import string

from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGui(QMainWindow):

    def __init__(self):
        super(MyGui,self).__init__()
        uic.loadUi("work.ui",self)
        self.pushButton.clicked.connect(self.passgen)
        self.pushButton_2.clicked.connect(self.copy_to_clipboard)
        self.show()

    def passgen(self):
        pswd=""
        small_alphabets = string.ascii_lowercase
        capital_alphabets = string.ascii_uppercase
        numbers = string.digits
        special_characters = string.punctuation

        weak = small_alphabets+capital_alphabets
        medium = small_alphabets+capital_alphabets+numbers
        strong = small_alphabets+capital_alphabets+numbers+special_characters

        length = self.spinBox.value()

        if self.radioButton.isChecked():
            for i in range(length):
                pswd = pswd + random.choice(weak)

        elif self.radioButton_2.isChecked():
            for i in range(length):
                pswd = pswd + random.choice(medium)

        elif self.radioButton_3.isChecked():
            for i in range(length):
                pswd = pswd + random.choice(strong)


        self.lineEdit.setText(pswd)

    def copy_to_clipboard(self):

        pswd = self.lineEdit.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(pswd)




app = QApplication([])
window = MyGui()
app.exec_()
