import turtle

turtle.setup(400, 500)
window = turtle.Screen()
window.title("Raphael becomes a traffic light!")
window.bgcolor("lightgreen")
raphael = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    raphael.pensize(3)
    raphael.color("black", "darkgrey")
    raphael.begin_fill()
    raphael.forward(80)
    raphael.left(90)
    raphael.forward(200)
    raphael.circle(40, 180)
    raphael.forward(200)
    raphael.left(90)
    raphael.end_fill()


draw_housing()
raphael.penup()
# Position tess onto the place where the green light should be
raphael.forward(40)
raphael.left(90)
raphael.forward(50)
# Turn tess into a big green circle
raphael.shape("circle")
raphael.shapesize(3)
raphael.fillcolor("green")
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0

# This variable holds the current state of the machine
pensize = 3


def advance_state_machine():
    """ Advances the state of the machine, changing
         it's color and position"""
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        raphael.forward(70)
        raphael.fillcolor("orange")
        state_num = 1
    elif state_num == 1:  # Transition from state 1 to state 2
        raphael.forward(70)
        raphael.fillcolor("red")
        state_num = 2
    else:  # Transition from state 2 to state 0
        raphael.back(140)
        raphael.fillcolor("green")
        state_num = 0


def blue_color():
    """ Change the fill color of turtle raphael to blue"""
    raphael.fillcolor("blue")


def green_color():
    """ Change the fill color of turtle raphael to green"""
    raphael.fillcolor("green")


def red_color():
    """ Change the fill color of turtle raphael to red"""
    raphael.fillcolor("red")


def increase_pensize():
    """ Increase the pensize of turtle raphael, to a maximum of 20"""
    global pensize
    pensize = pensize + 1
    if pensize >= 20:
        pensize = 20
    raphael.pensize(pensize)


def decrease_pensize():
    """ Decrease the pensize of turtle raphael, to a minimum of 1"""
    global pensize
    pensize = pensize - 1
    if pensize <= 1:
        pensize = 1
    raphael.pensize(pensize)


def change_circle():
    """ Change the shape of turtle raphael to a circle """
    raphael.shape("circle")


def change_square():
    """ Change the shape of turtle raphael to a square """
    raphael.shape("square")


def change_turtle():
    """ Change the shape of turtle raphael to a turtle """
    raphael.shape("turtle")


# Bind the event handler to the space key.
window.onkey(advance_state_machine, "space")
window.onkey(blue_color, "b")
window.onkey(green_color, "g")
window.onkey(red_color, "r")
window.onkey(increase_pensize, "plus")
window.onkey(decrease_pensize, "minus")
window.onkey(change_circle, "c")
window.onkey(change_square, "s")
window.onkey(change_turtle, 't')
window.listen()  # Listen for events
window.mainloop()
