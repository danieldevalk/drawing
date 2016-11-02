import turtle

my_screen = turtle.Screen()
my_turtle = turtle.Turtle()

coord_list_1 = [[-200,200],[-200,90],[-50,-20]]
coord_list_2 = [[50,200],[50,170],[300,90],[50,30],[50,0],[50,-13],[50,-73]]

def draw_bipartite_graph(coord_list_1, coord_list_2):
    for line in range(len(coord_list_1)):
        my_turtle.up()
        my_turtle.setposition(coord_list_1[line])
        my_turtle.down()
        for lines in range (len(coord_list_2)):
            my_turtle.setposition(coord_list_2[lines])
            my_turtle.setposition(coord_list_1[line])

draw_bipartite_graph(coord_list_1, coord_list_2)

def draw_stick_figure(headsize):
    my_turtle.up()
    my_turtle.setposition(-300, 0)
    my_turtle.down()
    my_turtle.seth(0)
    my_turtle.circle(headsize)
    draw_body(headsize)
    draw_arms(headsize)
    draw_legs(headsize)
def draw_body(headsize):
    my_turtle.seth(270)
    my_turtle.fd(headsize*4)
def draw_arms(headsize):
    my_turtle.left(180)
    my_turtle.fd(headsize*3)
    my_turtle.left(135)
    my_turtle.fd(headsize*2)
    my_turtle.left(180)
    my_turtle.fd(headsize*2)
    my_turtle.right(90)
    my_turtle.fd(headsize*2)
    my_turtle.left(180)
    my_turtle.fd(headsize*2)
def draw_legs(headsize):
    my_turtle.left(135)
    my_turtle.fd(headsize*3)
    my_turtle.right(45)
    my_turtle.fd(headsize*2)
    my_turtle.bk(headsize*2)
    my_turtle.left(90)
    my_turtle.fd(headsize*2)
def draw_spiral(x_position, y_position, spiral_size):
    my_turtle.seth(0)
    my_turtle.up()
    my_turtle.setposition(x_position,y_position)
    my_turtle.down()
    count=0
    coordinates_x=625
    coordinates_y=585
    while coordinates_x>spiral_size*2:
        my_turtle.color("green")
        my_turtle.begin_fill()
        my_turtle.fd(625-(count*spiral_size))
        coordinates_x=625-(count*spiral_size)
        my_turtle.right(90)
        my_turtle.fd(585-(count*spiral_size))
        coordinates_y=585-(count*spiral_size)
        my_turtle.right(90)
        count=count+1
    my_turtle.up()
    my_turtle.color("black")
def draw_sun(x_position, y_position, sun_size):
    count=0
    my_turtle.up()
    my_turtle.setposition(x_position,y_position)
    my_turtle.color("yellow")
    my_turtle.down
    my_turtle.begin_fill()
    my_turtle.circle(sun_size)
    my_turtle.end_fill()
    my_turtle.up()
    my_turtle.left(90)
    my_turtle.fd(sun_size)
    my_turtle.down()
    while count<36:
        my_turtle.fd(sun_size*2)
        my_turtle.bk(sun_size*2)
        my_turtle.right(10)
        count=count+1

    my_turtle.fd(50)
def draw_full_rectangle(x_position, y_position, rectangle_height, rectangle_length):
    my_turtle.up()
    my_turtle.setposition(x_position, y_position)
    my_turtle.down()
    count=0
    my_turtle.fillcolor("black")
    my_turtle.begin_fill()
    while count<2:
        my_turtle.fd(rectangle_length)
        my_turtle.right(90)
        my_turtle.fd(rectangle_height)
        my_turtle.right(90)
        count=count+1
    my_turtle.end_fill()


draw_spiral(-100,295,30)
draw_full_rectangle(-200,100,30,40)
draw_stick_figure(25)
draw_sun(-225,185,50)
