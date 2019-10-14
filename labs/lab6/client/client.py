from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QAction
import sys
import socket
from lab6.server.question import Question
import json


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('lab6.ui', self)
        self.handler = Handler(self)
        self.chosen_answer = 0

        self.quizLayout = self.findChild(QtWidgets.QVBoxLayout, 'quizLayout')

        self.errorLabel = self.findChild(QtWidgets.QLabel, 'errorLabel')
        self.scoreLabel = self.findChild(QtWidgets.QLabel, 'scoreLabel')
        self.quizText = self.findChild(QtWidgets.QTextBrowser, 'quizText')

        btnContainer = self.errorLabel.parent()
        self.buttons = []
        for i in range(3):
            btn = btnContainer.findChildren(QtWidgets.QPushButton)[i]
            self.buttons.append(btn)

        send0 = lambda: self.handler.send_answer(self.buttons[0].text())
        send1 = lambda: self.handler.send_answer(self.buttons[1].text())
        send2 = lambda: self.handler.send_answer(self.buttons[2].text())
        self.buttons[0].clicked.connect(send0)
        self.buttons[1].clicked.connect(send1)
        self.buttons[2].clicked.connect(send2)

        self.scoreLabel.setVisible(False)
        self.errorLabel.setVisible(False)

        self.handler.start()
        self.show()

    def show_question(self, question_text: str, answer_list: list):
        self.quizText.setText(question_text)
        self.buttons[0].setText(answer_list[0])
        self.buttons[1].setText(answer_list[1])
        self.buttons[2].setText(answer_list[2])

    def send_answer(self, answer_text: str):
        self.handler.send_answer(answer_text)

    def show_result(self, num_right: int):
        self.scoreLabel.setText('Ваш результат: {}'.format(num_right))
        self.scoreLabel.setVisible(True)


class Handler:
    HOST = 'localhost'
    PORT = 1235

    def __init__(self, ui: UI):
        self.ui = ui
        self.socket = None

    def connect(self):
        self.socket = socket.socket()
        self.socket.connect((self.HOST, self.PORT))
        print('Client connected')

    def disconnect(self):
        if self.socket is not None:
            self.socket.close()
            print('Closed client connection')

    def send_answer(self, answer_text: str):
        self.socket.send(answer_text.encode('utf-8'))
        self.request_question()

    def request_question(self):
        server_msg = str(self.socket.recv(1024).decode())
        is_end = 'num_right' in server_msg

        if is_end:
            result = json.loads(server_msg)
            self.ui.show_result(result['num_right'])
            self.disconnect()
        else:
            question = Question.from_json(server_msg)
            self.ui.show_question(question.text, question.answers)

    def start(self):
        self.connect()
        self.request_question()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec()
