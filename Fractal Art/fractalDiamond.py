from turtle import *

speed(0)

def side(length, levels):
    if levels == 0:
        forward(length)
        return
    
    length /= 4

    side(length, levels-1)
    left(90)
    side(length, levels-1)
    right(180)
    side(length, levels-1)
    left(90)
    side(length, levels-1)

def createDiamond(length):
    color("red")
    for i in range(4):
        side(length, 3)
        right(90)

    setpos(length / 8,0)

    color("blue")
    for i in range(4):
        side(length * -1, 3)
        right(-90)
    pass

createDiamond(1200)
mainloop()