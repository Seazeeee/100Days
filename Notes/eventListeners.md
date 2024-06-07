# Turtle Event Listeners

A listener is something that is listen for events to be triggered by user or
application.

```python

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    time.forward(10)


screen.listen() # Start the listener

# This means that when the key "space" is pressed it will trigger the function move_forward.
screen.onkey(key="space", fun=move_forwards) # You don't need to call the () utilizing 
#a function inside another function. This is shown above,

screen.exitonclick()
```

### Functions as Inputs

```python

def function_a(something):
    # Do this with something
    # Then do this
    # Finally do this

def function_b():
    # Do this

function_a(function_b) # When we pass the function as an input, we don't need the ().

```

### Higher Order Functions

- A function that can work with other functions. Calculators are good examples because it
can take a function and use it inside of another function.

- You should use Keywords Arguments instead of positional arguments in functions that you
haven't created just to make sure you know exactly what is happening.