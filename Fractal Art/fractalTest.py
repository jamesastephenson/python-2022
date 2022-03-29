# Import the turtle module
  # it is a 2d graphics module that lets you do visuals
from turtle import *

# turtle has a cursor that starts at 0,0 and draws a line when you move it
shape("turtle")

# speed accepts 1-10, 1 is slowest, 10 and 0 are fastest
speed(3)

# defining a fractal tree using recursion
  # we need to go back with recursion to draw each branch
def tree(size, levels, angle):
    # base case: telling us when to stop (prevent infinite loop)
    if levels == 0:
        color("green")
        # dot function will make a dot with a radius of the argument var (size)
            # REMEMEBER: this appears when our base case is hit
        dot(size)
        return

    # going forward by whatever the tree size argument is
    forward(size)

    # DRAW RIGHT BRANCH OF TREE
    # turn right by angle
    right(angle)

    # pass 80% of prev size to scale down
    # also subtract from levels to bring smaller
    tree(size * 0.8, levels - 1, angle)

    # DRAW LEFT BRANCH OF TREE
    left(angle * 2)
    tree(size * 0.8, levels - 1, angle)

    # straighten position back up by using right again
    right(angle)
    # go backwards to go back to start position
    backward(size)

# turning it 90 deg for start pos 
left(90)
tree(100, 6, 30)

# mainloop() function prevents turtle from closing instantly
mainloop()

# -------------- BASIC MOVEMENT EXAMPLES ------------
# basic movement facing right
#forward(100)
# left will turn X degrees relative to where we're facing
#left(45)
# to go up now, we will use forward again
#forward(100)
# try right again
#right(90)
#forward(100)
#backward(200)