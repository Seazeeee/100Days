"""
    This will most be written for 
    Hurdle = https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
    
    Maze = https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
    """

def reeborg_hurdle():
    def turn_right():
        turn_left()
        turn_left()
        turn_left()
        
    def jump():
        if wall_on_right() and front_is_clear():
            move()
        elif wall_in_front() and wall_on_right():
            turn_left()
        else:
            turn_right()
            move()
            turn_right()
            move()
            if not wall_in_front():
                move()
            else:
                turn_left()

    while not at_goal():
        if wall_in_front() or right_is_clear():
            jump()
        else:
            move()



def rebborg_maze():
    def turn_right():
            turn_left()
            turn_left()
            turn_left()

    while front_is_clear():
        move()
    turn_left()
        
    while not at_goal():
        if wall_on_right() and front_is_clear():
            move()
        elif wall_on_right() and wall_in_front():
            turn_left()
        else:
            turn_right()
            move()

