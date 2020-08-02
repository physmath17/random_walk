# Random walk simulator on an infinite two dimensional lattice with N steps each of step size 1

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from datetime import datetime

# parameters
start = np.array([float(item) for item in input("Enter the starting coordinates (separated by spaces) : ").split()]) # starting point of the walk
N = int(input("Enter the (maximum) number of steps : "))                                                # (maximum) number of steps
size = int(input("Enter the ensemble size (number of walkers or number of times the walk is repeated) : "))          # ensemble size 

startTime = datetime.now()

# function definitions
def random_walk_2D_lattice(n, z) :
    """ simulates an n-step two dimensional random walk on a lattice with an ensemble size z
    n : positive integer, z : positive integer (larger the z value more accurate is the simulation) 
    returns a (z, 2) array of the endpoints of the walk"""

    global start
    
    end = np.zeros((z, 2))                              # stores the endpoints of the walks
    for j in range(1, z) :                              # loops through the number of ensemble size
        walk = start                                    # initializing the walk
        for i in range(n) :                             # loops through the number of steps
            r = np.random.rand()    # random number to decide whether the walker goes left or right
            walk = (walk + [1, 0])*(r < 0.25) + (walk + [-1, 0])*(r > 0.25 and r < 0.5) + (walk + [0, 1])*(r > 0.5 and r < 0.75) + (walk + [0, -1])*(r > 0.75 and r < 1)     # describes the walk
        end[j] = walk

    return end

def mean_sq_distance(points) :
    """ returns the mean-squared distance from the starting point 
    points : (z, 2) array """

    global size

    sq = 0
    for i in range(size) :
        sq += points[i][0]**2 + points[i][1]**2
    mean = sq / size
    
    return mean

# result for fixed N simulation
end_points = random_walk_2D_lattice(N, size)
print(end_points)
plt.hist2d(end_points[:,0], end_points[:,1], bins=20)
plt.colorbar()
plt.show()

# result for mean squared distance vs N
dist_sq = np.array([0. for x in range(N + 1)])
n = np.array([x for x in range(N + 1)])

for i in range(N + 1) :
    data = random_walk_2D_lattice(i, size)
    dist_sq[i] = mean_sq_distance(data)

plt.plot(n, dist_sq)
plt.scatter(n, dist_sq)
plt.xlabel("number of steps")
plt.ylabel("mean squared distance from origin")
plt.xticks(n)
plt.show()

endTime = datetime.now()

print("Execution time : ", endTime - startTime)