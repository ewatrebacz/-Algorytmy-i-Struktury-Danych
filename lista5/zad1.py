import numpy as np
from scipy import linalg
import random
import time
import matplotlib.pyplot as plt
from scipy import stats

def solve(matrix, vector):
    '''solve the system of equations using linalg.solve'''
    return linalg.solve(matrix, vector)

x = []
y = []

for i in range(2,1001):
    new_y = []
    for j in range(0, 5):
        a = np.random.rand(i,i)
        b = np.random.rand(i,1)
        start = time.time()
        solve(a, b)
        end = time.time()
        new_y.append(end - start)
    new_time = 0
    for k in range(0, len(new_y)):
        new_time += new_y[k]
    x.append(i)
    y.append(new_time / len(new_y))
    new_y = []

x_log = list(map(np.log2, x))
y_log = list(map(np.log2, y))
res = stats.linregress(x_log[500:], y_log[500:])
plt.scatter(x_log[500:], y_log[500:])
y_log_2 = []
for i in range(0, len(x_log)):
    y_log_2.append(res.intercept + res.slope*x_log[i])
plt.plot(x_log[500:], y_log_2[500:], 'r')
plt.show()

print(res.slope)

