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
     it's color and position every second """
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
    window.ontimer(advance_state_machine, 1000)


# Bind the event handler to the space key.
window.ontimer(advance_state_machine, 1000)
window.listen()  # Listen for events
window.mainloop()
