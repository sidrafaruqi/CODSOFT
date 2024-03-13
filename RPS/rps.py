from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import random
import sys
import os


class MainWindow(QMainWindow):
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    def __init__(self):
        super().__init__()
        uic.loadUi("play.ui", self)
        self.pushButton.clicked.connect(self.start_game)

    def start_game(self):
        try:
            self.game_window = GameWindow()
            self.game_window.show()
            self.close()
        except Exception as e:
            print("An error occurred:", e)


class MainWindow(QMainWindow):
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    def __init__(self):
        super().__init__()
        uic.loadUi("play.ui", self)
        self.pushButton.clicked.connect(self.start_game)

    def start_game(self):
        try:
            self.game_window = GameWindow()
            self.game_window.show()
            self.close()
        except Exception as e:
            print("An error occurred:", e)


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gamewindow.ui", self)
        self.pushButton.clicked.connect(self.play_r)
        self.pushButton_2.clicked.connect(self.play_p)
        self.pushButton_3.clicked.connect(self.play_s)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_text)
        self.timer.setSingleShot(True)
        self.score = 0
        self.compscore = 0
        self.rounds = 0

    def highscore(self):
        with open("score.txt", "a+") as s:
            s.seek(0)
            hs = s.readline()
            if hs:
                p = [int(x) for x in hs.split(",")]

            if self.score > p[0]:
                with open("score.txt", "w") as s:
                    s.write(str(self.score) + "," + str(self.score))
            else:
                with open("score.txt", "w") as s:
                    s.write(str(p[0]) + "," + str(self.score))

    def check(self):
        if self.rounds >= 10:
            try:
                self.hs = HighScoreWindow()
                self.hs.show()
                self.close()
            except Exception as e:
                print("An error occurred:", e)
            self.close()  # Close the window
        self.highscore()

    def play_r(self):
        self.play_rps('r')

    def play_p(self):
        self.play_rps('p')

    def play_s(self):
        self.play_rps('s')

    def play_rps(self, player_choice):
        rps = "rps"
        computer = random.choice(rps)

        if computer == player_choice:
            result = "IT'S A DRAW!"
        elif (player_choice == 'r' and computer == 's') or \
                (player_choice == 'p' and computer == 'r') or \
                (player_choice == 's' and computer == 'p'):
            result = "YOU WIN!"
            self.score += 10
        else:
            result = "YOU LOSE!"
            self.compscore += 10

        self.lineEdit.setText(f"THE COMPUTER CHOSE {computer.upper()}!")
        self.lineEdit_4.setText(result)
        self.lineEdit_2.setText(str(self.score))
        self.lineEdit_3.setText(str(self.compscore))
        self.timer.start(1000)  # Set a 1 second delay
        self.rounds += 1
        self.check()

    def update_text(self):
        self.lineEdit.setText("YOUR TURN!")
        self.lineEdit_4.setText("RESULT!")


class HighScoreWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("score.ui", self)
        self.pushButton.clicked.connect(self.retry)

        with open("score.txt", "r") as s:
            s.seek(0)
            hs = s.readline()
            if hs:
                p = hs.split(",")
        self.lineEdit_4.setText(p[0])
        self.lineEdit_5.setText(p[1])


    def retry(self):
        self.game_window = GameWindow()
        self.game_window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
