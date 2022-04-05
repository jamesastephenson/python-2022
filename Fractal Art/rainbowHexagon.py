import turtle
import colorsys

# store drawing object and screen in variables
poly = turtle.Turtle()
screen = turtle.Screen()

# set background and speed
screen.bgcolor("black")
poly.speed(0)


for i in range(500):
    # change hue value in hsv each loop, saturation and value stay the same
    color = colorsys.hsv_to_rgb((0.8 * i)/400, 1, 1)
    # set color
    poly.pencolor(color)
    # draw line (length based on i value)
    poly.forward((9 * i) / 2)
    # turn
    poly.left(59)

turtle.done()