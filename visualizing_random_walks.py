import numpy as np
import matplotlib.pyplot as plt

# parameters
N = int(input("Enter the (maximum) number of steps : "))                                                            # (maximum) number of steps
prob = float(input("Enter the probability to move to the right : "))                                                # probability of taking a step to the right


def walk_one_dim(n, p) : 
    """ n : integer, p : float (probability to go right) 
    returns an array of size n - the path
    gives a visual representation of the two dimensional random walk with n steps """

    walk = np.array([np.float64(x) for x in range(0)])
    s = 0
    for i in range(n) :                             # loops through the number of steps
        r = np.random.rand()                        # random number to decide whether the walker goes left or right
        s += 1*(r<p) + (-1)*(r>p)                      # describes the walk
        walk = np.append(walk, [s])
    return walk


path = walk_one_dim(N, prob)
steps = np.linspace(0, N, N)
plt.scatter(steps, path, alpha=0.2, marker=',')
plt.show()