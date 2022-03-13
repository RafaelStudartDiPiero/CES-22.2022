import turtle


def draw_square(t, n):
    """ Makes a turtle t draw a square with length n"""
    for i in range(4):
        t.forward(n)
        t.left(90)


def multiple_concentric_squares(t, n, r, i):
    """ Makes a turtle t draw i squares with starting size of n and the size increases by
    r"""
    for j in range(i):
        draw_square(t, n)
        n += r
        t.penup()
        t.goto(t.xcor()-r/2, t.ycor()-r/2)
        t.pendown()


window = turtle.Screen()
window.bgcolor("lightgreen")
raphael = turtle.Turtle()
raphael.color("hotpink")
raphael.pensize(3)
raphael.pencolor("hotpink")

multiple_concentric_squares(raphael, 20, 20, 5)

window.mainloop()


