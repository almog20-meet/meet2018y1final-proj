import time
import turtle
import random


turtle.tracer(1,0)
turtle.setup(750, 1050)



#part 1
#difine
paper_pos_list = []
score = 0
level = 1
live = 3
x_t_bin_pos= 0
y_t_bin_pos= -450
my_pos = (x_t_bin_pos, y_t_bin_pos)
#make pos for trash bin

T_BIN_SIZE = 20

LEFT_ARROW = "Left" 
RIGHT_ARROW = "Right"

RIGHT= 0
LEFT=1
direction = RIGHT
UP_EDGE = 500
DOWN_EDGE = -500
RIGHT_EDGE = 300
LEFT_EDGE = -300

t_bin = turtle.Turtle()
t_bin.shape("circle")

paper = turtle.Turtle()
paper.shape("turtle")

trash = turtle.clone()
trash.shape("square")
t_bin.penup()

border = turtle.clone()
border.width(20)
border.hideturtle()
border.penup()
border.goto(-300, 500)
border.pendown()
border.goto(-300,-500)
border.goto(300,-500)
border.goto(300,500)
border.goto(-300,500)


#part2

t_bin.goto(x_t_bin_pos, y_t_bin_pos)

#MOVE TRASHH BIN 
#right
def right():
    global  direction
    direction=RIGHT
    move_t_bin()
    print("you pressed the right key")

#LEFT
def left():
    global  direction
    direction=LEFT
    move_t_bin()
    print("you pressed the left key")

turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.listen()

def move_t_bin():
    my_pos = t_bin.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = t_bin.pos()
    new_x_pos = my_pos[0]
    new_y_pos = my_pos[1]
    global RIGHT_EDGE, LEFT_EDGE, direction
    if direction==RIGHT:
        t_bin.goto(new_x_pos + T_BIN_SIZE, y_t_bin_pos)
        print("You moved right!")
        my_pos=(new_x_pos + T_BIN_SIZE, y_t_bin_pos)
    elif direction==LEFT:
        t_bin.goto(new_x_pos - T_BIN_SIZE, y_t_bin_pos)
        print("You moved left!")
        my_pos=(new_x_pos - T_BIN_SIZE, y_t_bin_pos)

while new_x_pos >= RIGHT_EDGE:
    direction = None        

while new_x_pos <= LEFT_EDGE:
    direction = None


