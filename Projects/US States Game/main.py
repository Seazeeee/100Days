import turtle
import pandas as df
from write_state import WriteStates
from reprompt import prompt


# Setting up screen variables and background.
BG_IMAGE = "Projects/US States Game/blank_states_img.gif"
correct_guesses: list[str] = []
question_prompt = prompt()
GAME_ON = True

SCREEN = turtle.Screen()
SCREEN.title("U.S. States Game")
SCREEN.addshape(BG_IMAGE)
turtle.shape(BG_IMAGE)

# Read the CSV

DATA = df.read_csv("Projects/US States Game/50_states.csv")

STATE_LIST = DATA["state"].to_list()

while GAME_ON:

    print(correct_guesses)

    question_answer = question_prompt.count_prompt()

    if question_answer in STATE_LIST:

        check_answer = DATA["state"][
            DATA.state.str.lower() == str(question_answer).lower()
        ].any()

        if check_answer:
            WriteStates(question_answer)
            correct_guesses.append(str(question_answer).strip().title())

    elif question_answer not in STATE_LIST:

        if question_answer is None:

            GAME_ON = False
            turtle.mainloop()

        else:

            question_prompt.wrong()

            continue
