"""
Random walk simulator in two dimensions with N steps each of step size 1

there are many ways to implement the two dimensional random walk :
1. think of the 2D random walk as two independent walks in  x and y direction with x and y distributed between [0, 1] such that sum of their square is unity
2. x = cos (t) and y = sin (t) with t distributed between [0, 2*pi]

We will use the latter approach to implement the walk.
"""

import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt
from numba import jit
from scipy.stats import norm
from datetime import datetime

# parameters
x0 = float(input("Enter the x-coordinate of the starting position : "))  
y0 = float(input("Enter the y-coordinate of the starting position : "))  
N = int(input("Enter the (maximum) number of steps : "))                                                            # (maximum) number of steps
size = int(input("Enter the ensemble size (number of walkers or number of times the walk is repeated): "))          # ensemble size 

startTime = datetime.now()

# function definitions
@jit(nopython=True)
def random_walk_two_dim(n, z) :
    """ simulates an n-step two dimensional random walk with an ensemble size z,
    n : positive integer, z : positive integer 
    returns a (z, 2) aray of endpoints of the walks"""

    global x0, y0

    end = np.zeros((z, 2))
    end[0] = [x0, y0]
    for j in range(1, z) :
        x, y = x0, y0
        for i in range(n) :
            s = np.random.rand()
            t = 2*pi*s
            x += cos(t)
            y += sin(t)
        end[j][0] = x
        end[j][1] = y

    return end
    
# @jit(nopython=True)
# def rms_distance(points, z) :
#     """ returs the root-mean-squared distance from the starting point 
#     z: integer, end_points : (z, 2) array """

#     sq = 0
#     for i in range(z) :
#         sq += points[i][0]**2 + points[i][1]
#     mean = sq / z
#     rms = np.sqrt(mean)
#     return rms

@jit(nopython=True)
def mean_sq_distance(points, z) :
    """ returns the mean-squared distance from the starting point 
    z: integer, end_points : (z, 2) array """

    sq = 0
    for i in range(z) :
        sq += points[i][0]**2 + points[i][1]**2
    mean = sq / z
    
    return mean

# result for mean squared distance vs N
dist_sq = np.array([0. for x in range(N + 1)])
n = np.array([x for x in range(N + 1)])

for i in range(N + 1) :
    data = random_walk_two_dim(i, size)
    dist_sq[i] = mean_sq_distance(data, size)

plt.plot(n, dist_sq)
plt.scatter(n, dist_sq)
plt.xlabel("number of steps")
plt.ylabel("mean squared distance from origin")
plt.xticks(n)
plt.show()

endTime = datetime.now()

# result for fixed N simulation


print("Execution time : ", endTime - startTime)