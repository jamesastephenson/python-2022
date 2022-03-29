from turtle import *

speed(0)
def snowflakeSide(length, levels):
    if levels == 0:
        forward(length)
        return

    # divide length by 3
    length /= 3.0

    # keep top level calls in mind
        # essentially we are subtracting from levels to get to our base case
        # our base case is where it actually draws a line (forward(length))
    # notice also that length keeps getting smaller on these recursive calls
        # -this allows for those "divet" triangles to be drawn to correct size
        # -dividing means it will be relative to what we start with
    # the deg turns happen after recursive calls so that we can draw the next "side"
        # -basically combining a standard line pattern and connecting it at angles
    snowflakeSide(length, levels - 1)
    left(60)
    snowflakeSide(length, levels - 1)
    right(120)
    snowflakeSide(length, levels - 1)
    left(60)
    snowflakeSide(length, levels - 1)


def createSnowflake(sides, length):
    colors = ["black", "blue", "green", "pink", "red", "orange"]
    for i in range(sides):
        color(colors[i])
        # notice that "sides" being passed in is the levels argument of snowflakeSides
        snowflakeSide(length, sides)
        # rotates where the next side is drawn based on how many sides we have
            # angle at 360 divided by our total number of sides
        right(360 / sides)
    pass

# note: remember adding more sides will exponentially create more small-sides
createSnowflake(3, 200)
mainloop()