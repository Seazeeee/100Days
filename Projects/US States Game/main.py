import turtle
import pandas as df
from write_state import WriteStates
from reprompt import Prompt


# Setting up screen variables and background.
BG_IMAGE = "Projects/US States Game/blank_states_img.gif"
correct_guesses: list[str] = []
question_prompt = Prompt()

SCREEN = turtle.Screen()
SCREEN.title("U.S. States Game")
SCREEN.addshape(BG_IMAGE)
turtle.shape(BG_IMAGE)

# Read the CSV
DATA = df.read_csv("Projects/US States Game/50_states.csv")

# Create a list of states to verify answer
STATE_LIST = DATA["state"].to_list()

# Create a loop until the total amount of states are reached.
while len(correct_guesses) < 50:
    # Print out the correct guess list
    print(correct_guesses)

    # Re-prompt the user every time it loops.
    question_answer = question_prompt.count_prompt()

    # Verifies that is not "None" because that means cancel is clicked.
    if question_answer is None:

        # If cancel is clicked we end the loop and turn the game off.
        break
    # Check is the given answer to question is in our state list.
    elif question_answer.title() in STATE_LIST:

        # Checks for duplicate answers.
        if question_answer.title() in correct_guesses:
            question_prompt.wrong()
            continue

        # Calls to write the states name in the given coords.
        WriteStates(question_answer)

        # Appends the name of the correct state.
        correct_guesses.append(str(question_answer).strip().title())

    # Checks if answer is not in the state list.
    elif question_answer not in STATE_LIST:
        # Creating a method to break
        if question_answer.lower() == "exit":

            # Finds all the missing states from answers
            missing_states = DATA[~DATA["state"].isin(correct_guesses)]["state"]

            # Takes those states and creates another CSV of "study" states.
            missing_states.to_csv("Projects/US States Game/states_to_learn.csv")

            break

        # Runs this command tha removes a count so that the correct
        # score stays.
        question_prompt.wrong()

        # Continues to re-run through the loop
        continue
