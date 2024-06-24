from turtle import Screen

SCREEN = Screen()


class prompt:

    def __init__(self) -> None:
        self.count = 0

    def count_prompt(self):
        if self.count == 0:
            answer_state_popup = SCREEN.textinput(
                title="Guess the State", prompt="What's another state's name?"
            )

            self.count += 1

            return answer_state_popup
        else:
            new_pop = SCREEN.textinput(
                title=f"{self.count}/50 States Correct",
                prompt="What's another state's name?",
            )

            self.count += 1

            return new_pop

    def wrong(self):

        self.count -= 1