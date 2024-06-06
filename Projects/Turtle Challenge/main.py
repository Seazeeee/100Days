from turtle import Turtle, Screen

casper = Turtle()

# First Challenge: Draw a square.
# for _ in range(4):
#     casper.forward(100)
#     casper.right(90)

# Second Challenge: Dotted Line
for _ in range(15):
    casper.forward(10)
    casper.penup()
    casper.forward(10)
    casper.pendown()


MY_SCREEN = Screen()
MY_SCREEN.exitonclick()
