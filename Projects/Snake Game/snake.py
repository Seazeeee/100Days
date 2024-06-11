from turtle import Turtle


class Snake:

    def __init__(self):
        self.dict_turtles = {}
        self.cords = [(0, 0), (-20, 0), (-40, 0)]
        self.index = 0

        for num_index in self.cords:
            # Create the different turtle methods needed; adds them to a dict.
            self.dict_turtles[self.index] = Turtle(shape="square")
            self.dict_turtles[self.index].penup()
            self.dict_turtles[self.index].color("white")
            self.dict_turtles[self.index].goto(num_index)
            self.index += 1
        print(self.dict_turtles)

    def move(self):
        for num_turtle in range(len(self.dict_turtles) - 1, 0, -1):
            # Grab the front turtle and its cords.
            forward_turtle = self.dict_turtles[num_turtle - 1]
            new_x = forward_turtle.xcor()
            new_y = forward_turtle.ycor()
            # Move the turtle behind to the new cords.
            self.dict_turtles[num_turtle].goto(x=new_x, y=new_y)
        self.dict_turtles[0].forward(20)
