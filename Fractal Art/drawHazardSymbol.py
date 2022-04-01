from turtle import *
speed(0)

# iterate through range, increase forward distance, keep turning right each loop
for i in range(1800):
    if i % 2 == 0:
        color("black")
    else:
        color("yellow")
    
    forward(2 + i / 4)

    # 60 deg each turn will make a hexagon shape
    right(60)

mainloop()