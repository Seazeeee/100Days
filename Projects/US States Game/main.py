import turtle
import pandas as df


# Setting up screen variables and background.
BG_IMAGE = "Projects/US States Game/blank_states_img.gif"
COUNT = 0
ALIGN = "center"
FONT = ("Courier", 10, "normal")

SCREEN = turtle.Screen()
SCREEN.title("U.S. States Game")
SCREEN.addshape(BG_IMAGE)
turtle.shape(BG_IMAGE)

answer_state_popup = SCREEN.textinput(
    title="Guess the State", prompt="What's another state's name?"
)

# Read the CSV

data = df.read_csv("Projects/US States Game/50_states.csv")

check_answer = data["state"][
    data.state.str.lower() == str(answer_state_popup).lower()
].any()

# print(check_answer)

if check_answer:

    x = data[data.state == str(answer_state_popup).title()].x.values[0]
    y = data[data.state == str(answer_state_popup).title()].y.values[0]

    # COUNT += 1

    # turtle.goto(
    #     x=x,
    #     y=y,
    # )

    turtle.write(
        arg=f"{str(answer_state_popup).title()}",
        align=ALIGN,
        font=FONT,
    )


turtle.mainloop()
