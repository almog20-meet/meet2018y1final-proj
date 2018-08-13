import time
import turtle

#part 1
#difin
paper_pos_list = []
score = 0
level = 1
live = 3
x_t_bin_pos= 0
y_t_bin_pos= -300
my_pos = (x_t_bin_pos, y_t_bin_pos)
#make pos for trash bin

T_BIN_SIZE = 5

LEFT_ARROW = "Left" 
RIGHT_ARROW = "Right"

RIGHT= 0
LEFT=1
direction = RIGHT


t_bin = turtle.Turtle()
t_bin.shape("circle")


paper =turtle.Turtle()
paper.shape("turtle")

trash=turtle.clone()
trash.shape("square")

t_bin.penup()



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

    global T_BIN_SIZE
    if direction==RIGHT:
        t_bin.goto(x_t_bin_pos + T_BIN_SIZE, y_t_bin_pos)
        print("You moved right!")
        my_pos=(x_t_bin_pos + T_BIN_SIZE, y_t_bin_pos)
    elif direction==LEFT:
        t_bin.goto(x_t_bin_pos - T_BIN_SIZE, y_t_bin_pos)
        print("You moved left!")
        my_pos=(x_t_bin_pos - T_BIN_SIZE, y_t_bin_pos)

    new_pos = t_bin.pos()
    new_x_pos = my_pos[0]
    new_y_pos = my_pos[1]
    

