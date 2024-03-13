import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

class MyMainWindow(QMainWindow):
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi("todo.ui", self)
        self.pushButton.clicked.connect(self.menu)

    def update(self):
        number = self.comboBox_3.currentText()
        new = self.lineEdit.text()


        if number == "1":
            self.lineEdit_2.setText(new)

        elif number == "2":
            self.lineEdit_5.setText(new)

        elif number == "3":
            self.lineEdit_3.setText(new)

        elif number == "4":
            self.lineEdit_4.setText(new)

        elif number == "5":
            self.lineEdit_6.setText(new)

        elif number == "6":
            self.lineEdit_7.setText(new)

        self.lineEdit.setText(" ")



    def delete(self):
        number = self.comboBox_3.currentText()
        new = " "

        if number == "1":
            self.lineEdit_2.setText(new)

        elif number == "2":
            self.lineEdit_5.setText(new)

        elif number == "3":
            self.lineEdit_3.setText(new)

        elif number == "4":
            self.lineEdit_4.setText(new)

        elif number == "5":
            self.lineEdit_6.setText(new)

        elif number == "6":
            self.lineEdit_7.setText(new)

    def delete_all(self):
        a = " "
        self.lineEdit_2.setText(a)
        self.lineEdit_3.setText(a)
        self.lineEdit_4.setText(a)
        self.lineEdit_5.setText(a)  # Corrected line
        self.lineEdit_6.setText(a)
        self.lineEdit_7.setText(a)


    def save(self):
        try:
            screenshot = QApplication.primaryScreen().grabWindow(self.winId())
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Screenshot", "", "Images (*.png *.jpg)")
            if file_name:
                screenshot.save(file_name)
                QMessageBox.information(self, "Screenshot Saved", "Screenshot saved successfully.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to save screenshot: {str(e)}")

    def menu(self):
        text = self.comboBox.currentText()

        if text == "UPDATE A TASK" or text == "ADD A TASK":
            self.update()

        if text == "DELETE A TASK":
            self.delete()

        if text == "DELETE ALL":
            self.delete_all()

        if text == "SAVE":
            self.save()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
