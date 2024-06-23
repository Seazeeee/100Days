import turtle
import pandas as df
from write_state import WriteStates
from reprompt import prompt


# Setting up screen variables and background.
BG_IMAGE = "Projects/US States Game/blank_states_img.gif"
COUNT = 0
correct_guesses = []
game_on = True

SCREEN = turtle.Screen()
SCREEN.title("U.S. States Game")
SCREEN.addshape(BG_IMAGE)
turtle.shape(BG_IMAGE)

answer_state_popup = SCREEN.textinput(
    title="Guess the State", prompt="What's another state's name?"
)

# Read the CSV

DATA = df.read_csv("Projects/US States Game/50_states.csv")

# check_answer = DATA["state"][
#     DATA.state.str.lower() == str(answer_state_popup).lower()
# ].any()


while game_on:

    if WriteStates.check_new(answer_state_popup):
        WriteStates(answer_state_popup)
        COUNT += 1
        correct_guesses.append(str(answer_state_popup).strip().title())
    prompt()

turtle.mainloop()
