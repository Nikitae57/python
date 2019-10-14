import json


class Question:
    def __init__(self, text: str, answers: list, right_answer: int):
        self.right_answer = right_answer
        self.answers = answers
        self.text = text

    def to_json(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)

    def from_json(json_str: str):
        loaded_json = json.loads(json_str)
        text = loaded_json['text']
        answers = loaded_json['answers']
        right_answer = loaded_json['right_answer']

        question = Question(text, answers, right_answer)
        return question


if __name__ == '__main__':
    json_str = '{"text": "asd", "answers": [1, 2, 3], "right_answer": 1}'
    a = Question.from_json(json_str)
