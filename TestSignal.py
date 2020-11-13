import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# Data for plotting

# t stands for time
t = np.arange(0, 100, 1)

# s is the function
s = 1 + np.sin(2 * np.pi * t)

# tells the module what to plot
fig, ax = plt.subplots()


#sets the xlabel,ylabel, and title
ax.set(xlabel='time (s)', ylabel='depression',title='lolmao')

#Makes the chart have a built-in grid
ax.grid()

# peak detection
peaks, _ = find_peaks(s, height=0)

# plots the graph
ax.plot(t,s)

#plots the peaks
ax.plot(peaks, s[peaks], "s")

#shows the graph
plt.show()