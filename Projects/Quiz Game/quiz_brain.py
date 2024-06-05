# TODO: Checking if we're the end of the quiz


class QuizBrain:

    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):

        selected_q = self.question_list[self.question_number]

        self.question_number += 1

        user_answer = input(
            f"Q.{self.question_number}: {selected_q.text} (True/False)?: ")

        if user_answer == selected_q.answer:
            return "Correct"
        return "Failed"
