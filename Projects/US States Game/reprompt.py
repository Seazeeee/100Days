from turtle import Screen

SCREEN = Screen()


class prompt:

    def __init__(self, count) -> None:
        self.count = count
        self.count_prompt()

    def count_prompt(self):
        new_pop = SCREEN.textinput(
            title=f"{self.count}/50 States Correct",
            prompt="What's another state's name?",
        )

        return new_pop
    
