import turtle


def draw_poly(t, n, sz):
    """ Makes a turtle t draw a regular polygon with n sides of size sz"""
    angle = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(angle)


# Examples

window = turtle.Screen()
window.bgcolor("lightgreen")
raphael = turtle.Turtle()
raphael.color("hotpink")
raphael.pensize(3)
raphael.pencolor("hotpink")

draw_poly(raphael, 8, 50)

window.mainloop()
