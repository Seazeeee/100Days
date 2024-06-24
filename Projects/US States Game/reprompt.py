"""Module that contains the prompt for the question."""
from turtle import Screen

SCREEN = Screen()


class prompt:

    """Houses the prompt for the guesses and keeps track of the score."""

    def __init__(self) -> None:
        self.count = 0

    def count_prompt(self):
        """Prompts the user. Then changes the prompt to include the
        score after the first prompt."""
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
        """Removes 1 from the count if they get the guess wrong. This
        keeps the score correct."""

        self.count -= 1