import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk()
rw.fillWalk() # make sure to call this so it actually generates

# Plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()
# give the walk's x and y values to scatter() and choose a dot size
    # remember that you're calling these using a class: hence rw.xValues etc
ax.scatter(rw.xValues, rw.yValues, s=15)
plt.show()