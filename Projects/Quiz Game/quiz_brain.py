# TODO: Checking if we're the end of the quiz


class QuizBrain:

    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.correct = 0
        self.question_list = question_list

    def still_has_questions(self) -> bool:
        """
        A method that returns True if there is still questions,
        False if there is not questions.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """A method that prints the question and checks the users input"""

        selected_q = self.question_list[self.question_number]

        self.question_number += 1

        user_answer = input(
            f"Q.{self.question_number}: {selected_q.text} (True/False)?: ")

        if user_answer == selected_q.answer:
            self.correct += 1
            print("You got it right!")
            print(f"The correct answer was: {selected_q.answer}")
            print(
                f"Your current score is: {self.correct}/{self.question_number}"
                )

        else:
            pass
