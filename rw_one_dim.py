# random walk simulator in one dimension

import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from scipy.stats import norm

# parameters
start = float(input("Enter the starting position : "))                                                              # starting point of the walk
N = int(input("Enter the (maximum) number of steps : "))                                                            # (maximum) number of steps
prob = float(input("Enter the probability to move to the right : "))                                                # probability of taking a step to the right
size = int(input("Enter the ensemble size (number of walkers or number of times the walk is repeated): "))          # ensemble size 

# function definitions
@jit(nopython=True)
def random_walk_one_dim(n, p, z) :
    """ simulates an n-step one dimensional random walk with an ensemble size z, p is the probability to go right
    n : positive integer, p : float, z : positive integer (larger the z value more accurate is the simulation) """

    global start
    
    end = np.array([np.float64(x) for x in range(0)])     # stores the endpoints of the walks
    for j in range(z) :                                 # loops through the number of ensemble size
        s = start                                       # initializing the walk
        for i in range(n) :                             # loops through the number of steps
            r = np.random.rand()                        # random number to decide whether the walker goes left or right
            s += 1*(r<p) + (-1)*(r>p)                      # describes the walk
        end = np.append(end, [s])
    
    return end

@jit(nopython=True)
def rms_distance(end_points) :
    """ returs the rms distance from the starting point """
    global size

    sq = 0
    for i in range(size) :
        sq += end_points[i]**2
    mean = sq / size
    rms = np.sqrt(mean)
    return rms

@jit(nopython=True)
def mean_sq_distance(end_points) :
    """ returs the mean squared distance from the starting point """
    global size

    sq = 0
    for i in range(size) :
        sq += end_points[i]**2
    mean = sq / size
    return mean

# result for fixed N simulation
points = random_walk_one_dim(N, prob, size)
print("The rms distance for {} steps is = {}".format(N, rms_distance(points)))

n, bins, _ = plt.hist(points, bins='auto', density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
mu, sigma = norm.fit(points)                                                                        # mean and standard devidation of Gaussian 
best_fit_line = (max(n) / max(norm.pdf(bins, mu, sigma)))*norm.pdf(bins, mu, sigma)                 # Gaussian fit to the histogram
plt.title(r"Histogram of random walk with N = %.i steps (fitted with $\mu = %.3f,\ \sigma = %.3f )$" %(N, mu, sigma))
plt.plot(bins, best_fit_line)
plt.xlabel("Position")
plt.ylabel("Probability Distribution")
plt.show()

# result for mean squared distance vs N
dist_sq = np.array([0. for x in range(3, N + 1)])
n = np.array([x for x in range(3, N + 1)])

for i in range(3, N + 1) :
    data = random_walk_one_dim(i, prob, size)
    dist_sq[i-3] = mean_sq_distance(data)

plt.plot(n, dist_sq)
plt.scatter(n, dist_sq)
plt.xlabel("number of steps")
plt.ylabel("mean squared distance from origin")
plt.xticks(n)
plt.show()