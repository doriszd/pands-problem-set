# Doris Zdravkovic, March, 2019
# Solution to problem 10

# Import numpy 
import numpy as np
# Import matplotlib.pyplot
import matplotlib.pyplot as plt
# x = range from 0 to 4 included
# 0 = beginning value of the range
# 5 = end of the range
x = np.arange(0, 5)
# plot - red, blue, green lines
# red = x, blue = x2, green = 2x
plt.plot(x,x, 'r--', x, x**2, 'b--', x, 2**x, 'g--')
# legend in upper left corner
plt.legend(['red = x', 'blue = x2', 'green = 2x'], loc='upper left')
plt.show()