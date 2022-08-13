# import library and abbreviate pyplot for easier use
import matplotlib.pyplot as plt

# list of data we'll be plotting
inputValues = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# using a built-in style
    # note: this needs to go BEFORE running subplots() and plot()
plt.style.use('dark_background')

# fig - represents entire figure (collection of plots generated)
# ax - represents a single plot (variable we'll use most of the time)
# subplots() - generate one or more plots in the same figure
fig, ax = plt.subplots() 

# plot() - will try to plot data its given in a meaningful way
# linewidth=3 argument controlling the line thickness of our plot
ax.plot(inputValues, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)


# show() opens matplotlib's viewer and displays the plot
plt.show()