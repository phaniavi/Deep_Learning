from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

def create_dataset(count, variance, step=2, correlation=False) :
    val = 1
    y = []
    for i in range(count) :
        temp = val + random.randrange(-variance, variance)
        y.append(temp)
        if correlation and correlation == 'pos' :
            val += step
        elif correlation and correlation == 'neg' :
            val -= step
    x = [i for i in range(len(y))]
    return np.array(x, dtype=np.float64), np.array(y, dtype=np.float64)

def best_fit_slope(x, y) :
    m = ( ((mean(x) * mean(y)) - mean(x * y)) / ((mean(x)**2) - mean(x**2)) )
    c = mean(y) - m * mean(x)
    return m,c

def squared_error(y_orig, y_line) :
    return sum((y_orig - y_line)**2)

def coefficient_of_determination(y_orig, y_line) :
    y_mean_line = [mean(y_orig) for y in y_orig]
    squared_error_regr = squared_error(y_orig, y_line)
    squared_error_y_mean = squared_error(y_orig, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)

x,y = create_dataset(50, 30, 2, False)

m,c = best_fit_slope(x,y)

regression_line = m * x + c

r_squared = coefficient_of_determination(y, regression_line)

print r_squared

plt.scatter(x, y)
plt.plot(x, regression_line, color='g')
plt.show()