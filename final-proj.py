import time
import turtle
import random







turtle.hideturtle()
min_x= -300
max_x= 300
min_y= -500
max_y= 500

turtle.tracer(1,0)
turtle.setup(750, 1050)

#lives
lives=turtle.Turtle()
lives.ht()
lives.penup()
lives.goto(250, 450)
turtle.register_shape("heart.gif")
lives.shape("heart.gif")
lives.st()
########fix this#####################################
lives1=turtle.Turtle()
lives1.ht()
lives1.penup()
lives1.goto(200, 450)
turtle.register_shape("heart.gif")
lives1.shape("heart.gif")
lives1.st()

#scorelabel
score=0
num_label=turtle.Turtle()
num_label.ht()
num_label.penup()
num_label.color("black")
num_label.width("5")
num_label.goto(-250, 420)
num_label.write(str (score),align="center",font=("Arial",40))         

# generates random x values for the falling items
def rand_x():
    return random.randint(min_x + 5, max_x - 5)
    
        #Pick a position that is a random multiple of SQUARE_SIZE
    pap_x = random.randint(min_x,max_x)*T_BIN_SIZE
    pap_y = 290
    pap.goto(pap_x,pap_y)
    pap_turtle_pos=(pap_x,pap_y)
    pap_pos.append(paper_turtle_pos)
    pap_stamp = pap.stamp()
    pap_stamps.append(food_stamp)#
    print(pap_pos)

# making paper and trash turtles
paper = turtle.clone()
turtle.register_shape("paperball.gif")
paper.shape("paperball.gif")
paper.penup()
paper.goto(rand_x(), min_y)

trash = turtle.clone() 
turtle.register_shape("banana.gif")
trash.shape("banana.gif")
trash.penup()
round_x = (rand_x()//20)*20
trash.goto(round_x, min_y)



#part 1
#difine#######################
DISTANCE = 10
paper_pos_list = []
pap_pos = []
score = 0
level = 1
live = 3
x_t_bin_pos= 0
y_t_bin_pos= -450
my_pos = (x_t_bin_pos, y_t_bin_pos)
my_turtles = [paper, trash]


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

 # bin turtle
turtle.register_shape("yhhhhh.gif")
t_bin = turtle.Turtle()
t_bin.shape("yhhhhh.gif")


t_bin.penup()

border = turtle.clone()
border.width(10)
border.hideturtle()
border.penup()
border.goto(-300, 500)
border.pendown()
border.goto(-300,-500)
border.goto(300,-500)
border.goto(300,500)
border.goto(-300,500)


def move_rand_turtle():
    for t in my_turtles:
        x,y = t.pos()
        t.goto(x,y-DISTANCE) # move papers in list down
    check_edge()    
    turtle.ontimer(move_rand_turtle, 100)

t_bin.goto(x_t_bin_pos, y_t_bin_pos)
if my_pos in pap_pos:
    paper.hideturtle()
    check_edge()
    pap_pos.pop[0]
    score = score+1

    print(score)

def check_edge():
    for t in my_turtles:
        x,y = t.pos()
        if y == 0 and len (my_turtles) <= 3:
            my_turtles.append(t.clone())
        if y <= -max_y:
            t.hideturtle()
            # decrease rate at which objects start falling by increasing range. Ex (1,20)
            if random.randint(1,35) == 10:
                t.goto(rand_x(), max_y)
                t.showturtle()
   


#MOVE TRASHH BIN 
#right
def right():
    global  direction
    direction=RIGHT
    if lock:
        move_t_bin()
    print("you pressed the right key")

#LEFT
def left():
    global  direction
    direction=LEFT
    if lock:
        move_t_bin()
    print("you pressed the left key")

turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.listen()

lock = True

def move_t_bin():
    global lock
    if lock:
        lock = False
        my_pos = t_bin.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        new_pos = t_bin.pos()
        new_x_pos = my_pos[0]
        new_y_pos = my_pos[1]
        global RIGHT_EDGE, LEFT_EDGE, direction
       # print(new_pos)
        if direction==RIGHT:
            if new_x_pos >= RIGHT_EDGE - 20: #-20 pixels to not get into the walls
                direction = None    #Checks if the t_bin inside the walls
                t_bin.goto(RIGHT_EDGE - T_BIN_SIZE, y_t_bin_pos)


            else:
                t_bin.goto(new_x_pos + T_BIN_SIZE, y_t_bin_pos)
                print("You moved right!")
                my_pos=(new_x_pos + T_BIN_SIZE, y_t_bin_pos)
        elif direction==LEFT:
            if new_x_pos <= LEFT_EDGE + 20: #+20 pixels to not get into the walls
                direction = None    #Checks if the t_bin inside the walls
                t_bin.goto(LEFT_EDGE + T_BIN_SIZE, y_t_bin_pos)

            else:
                t_bin.goto(new_x_pos - T_BIN_SIZE, y_t_bin_pos)
                print("You moved left!")
                my_pos=(new_x_pos - T_BIN_SIZE, y_t_bin_pos)
        lock = True

#paper in the bin
# def paper_in_bin():
    

        

move_rand_turtle()

turtle.mainloop()
