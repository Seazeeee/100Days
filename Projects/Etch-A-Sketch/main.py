# Requirements.
# A - Forward - Done
# S - Backwards - Done
# A - Counter-Clockwise
# D - Clockwise
# C - Clear

from turtle import Turtle, Screen

casper = Turtle()
SCREEN = Screen()


def move_forwards():
    """Move the turtle Forwards"""
    casper.forward(10)


def move_backward():
    """Move the turtle backwards"""
    casper.backward(10)


def move_clockwise():
    """Rotate the turtle clockwise"""
    casper.setheading(casper.heading() + 10)


def move_counter_clockwise():
    """Rotate the turtle counter-clockwise"""
    casper.setheading(casper.heading() - 10)


def clear():
    """Reset the drawing"""
    casper.reset()
    casper.clear()


SCREEN.listen()
SCREEN.onkey(key="w", fun=move_forwards)
SCREEN.onkey(key="a", fun=move_counter_clockwise)
SCREEN.onkey(key="s", fun=move_backward)
SCREEN.onkey(key="d", fun=move_clockwise)
SCREEN.onkey(key="c", fun=clear)
SCREEN.exitonclick()
