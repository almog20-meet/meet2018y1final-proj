import turtle
import random
#make turtles
turtle.tracer(1,0) #removes delay
adam = turtle.Turtle()
valeria = turtle.Turtle()
valeria.shape("square") # so you can tell which turtle is which
player = turtle.Turtle()
valeria.up()
adam.up()
my_turtles = [adam, valeria] # this important
#make constant values, display screen
WIDTH = 1000
HEIGHT = 700
MAX_X = WIDTH/2 - 20 # -20 so that falling items don't touch edges
MAX_Y = HEIGHT/2 -20 # -20 so that falling items don't touch edges
turtle.setup(WIDTH, HEIGHT) # makes a screen with width 1000, height 700
DISTANCE = 10 # how far the turtles move each time step (decrease to  move slower)
TIME_STEP = 10 # 10 milliseconds (1000 ms = 1 s) Increase to move slower


def move_turtle():
    for t in my_turtles:
        x,y = t.pos()
        t.goto(x,y-DISTANCE) # move turtles in list down
    # insert code to move player here! (Hint: it should be pretty similar to snake)
    check_edge() # check if turtles hit the bottom edge
    check_player() # check if player is hit by falling turtles
    turtle.ontimer(move_turtle, 10)

# generates random x values for the falling items
def rand_x():
    return random.randint(-MAX_X, MAX_X)
'''
Hides the turtle if it is below bottom edge
This turtle will continue to fall until 10 is randomly selected.
Think of it like rolling a 10 sided dice and waiting for a 10 to
be rolled. This causes the items to fall at random times.
'''
def check_edge():
    for t in my_turtles:
        x,y = t.pos()
        if y <= -MAX_Y:
            t.hideturtle()
            # decrease rate at which objects start falling by increasing range. Ex (1,20)
            if random.randint(1,10) == 10:
                t.goto(rand_x(),MAX_Y)
                t.showturtle()
#checks if player has been hit by falling turtle
def check_player():
    for t in my_turtles:
        if player.pos() == t.pos():
            quit()

# first time the turtles fall
for t in my_turtles:
    t.goto(rand_x(),-MAX_Y)

move_turtle() #this must be the last line of your code.
