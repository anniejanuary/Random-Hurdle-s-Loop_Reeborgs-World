def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    while wall_on_right() == True and front_is_clear() == True:
            move() 
    turn_right()
    move()
    turn_right()
    move()
    while wall_on_right() == True and front_is_clear() == True:
            move() 
    turn_left()

while at_goal() == False:
    if front_is_clear() == True:
        move()
    if wall_in_front() == True:
        jump()
   
