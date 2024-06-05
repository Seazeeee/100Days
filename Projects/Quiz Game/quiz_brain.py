class QuizBrain:
    """The brain behind the quiz that makes it function"""

    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.score = 0
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

        self.check_answer(user_answer, selected_q.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        A method that checks if the answer is right and prints out statements
        corresponding to each.
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        print(
            f"Your current score is: {self.score}/{self.question_number} \n\n"
        )
