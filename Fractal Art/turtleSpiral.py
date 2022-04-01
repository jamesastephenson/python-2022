from turtle import *
speed(0)

# iterate through range, increase forward distance, keep turning right each loop
for i in range(1800):
    if i % 2 == 0:
        color("red")
    else:
        color("blue")
    
    forward(2 + i / 4)
    right(15)

mainloop()