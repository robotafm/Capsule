from tkinter import *
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter
import csv

file_folder = "D:/Data/csv/"
file_name = "13_21 13.12.2021.csv"

# Mathplotlib:
def init():
    line.set_ydata([np.nan] * len(x))
    return line,

def animate(i):
    # Add next value
    data.append(np.random.randint(0, max_rand))
    line.set_ydata(data)
    # plt.savefig('e:\\python temp\\fig_{:02}'.format(i))
    print(i)
    return line,
information = []
with open(file_folder+file_name, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        information.append(row[0])

max_x = 1000
max_rand = 100

data = deque(np.zeros(max_x), maxlen=max_x)  # hold the last values
x = np.arange(0, max_x)

fig, ax = plt.subplots()
ax.set_ylim(0, max_rand)
ax.set_xlim(0, max_x-1)
line, = ax.plot(x, information)
# ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{:.0f}s'.format(max_x - x - 1)))
# plt.xlabel('Seconds ago')

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=10, blit=True, save_count=10)

plt.show()