import socket
import random
from lab6.server.question import Question
import json


class Handler:
    def __init__(self):
        self._questions = [
            Question('Кто из президентов США написал свой собственный рассказ про Шерлока Холмса?',
                     ['Джон Кеннеди', 'Франклин Рузвельт', 'Рональд Рейган'],
                     1),
            Question('Какую пошлину ввели в XII  веке в Англии для того чтобы заставить мужчин пойти на войну?',
                     ['Налог на тунеядство', 'Налог на трусость', 'Налог на отсутствие сапог '],
                     1),
            Question('Откуда пошло выражение «деньги не пахнут?',
                     ['От подателей за провоз парфюмерии', 'От сборов за нестиранные носки', 'От налога на туалеты'],
                     2),
            Question('Туристы, приезжающие на Майорку, обязаны заплатить налог…',
                     ['На плавки', 'На пальмы', 'На солнце'],
                     2),
            Question('Российский мультфильм, удостоенный «Оскара», — это…',
                     ['Старик и море', 'Винни-Пух', 'Простоквашино'],
                     0),
        ]

    def handle(self, conn: socket):
        randomized_questions = self._questions.copy()
        random.shuffle(randomized_questions)

        try:
            num_right = 0
            for question in randomized_questions:
                question_json = question.to_json()
                conn.send(question_json.encode('utf-8'))

                answer = conn.recv(1024).decode()
                if answer == question.answers[question.right_answer]:
                    num_right += 1

            quiz_results = {'num_right': num_right}
            quiz_results_json = json.dumps(quiz_results)
            conn.send(quiz_results_json.encode('utf-8'))

            conn.close()
        except socket.error:
            print('Socket error occurred!')


if __name__ == '__main__':
    h = Handler()
    h.handle(None)