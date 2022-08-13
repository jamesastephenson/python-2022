#import library and abbreviate
import matplotlib.pyplot as plt

# to plot a series of points, we can pass scatter() separate lists of xs and ys
    # here we are generating values with a range and a quick loop for the squares
xValues = range(1, 1001)
yValues = [x**2 for x in xValues] # iterating through xValues and squaring the val at that position

plt.style.use('seaborn')
fig, ax = plt.subplots()

# passing our point value lists into scatter()
# ax.scatter(xValues, yValues, c=(0,0.8,0), s=10) # s refers to size here, c is color

# using a colormap
    # c gets what we want to assign a colormap based on
    # cmap is where we apply the colormap itslef
ax.scatter(xValues, yValues, c=yValues, cmap=plt.cm.Blues, s=10)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# set range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()