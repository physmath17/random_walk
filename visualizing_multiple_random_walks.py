import numpy as np
from numpy import pi, sin, cos
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from datetime import datetime

def walk_one_dim() : 
    """ gives a visual representation of the one dimensional random walk with N steps """
    global w, N, prob, x0
    walk = np.zeros((N, 10))                            # stores the path of the 10 random walkers
    steps = np.linspace(0, N, N)
    for j in range(w) :
        s = x0[j]
        for i in range(N) :                             # loops through the number of steps
            r = np.random.rand()                        # random number to decide whether the walker goes left or right
            s += 1*(r<prob) + (-1)*(r>prob)             # describes the walk
            walk[i][j] = s
        plt.scatter(steps, walk[:,j], alpha=0.7, s=0.1)
    plt.title("1D random walk with {} steps, {} walkers, and {} probability to go up".format(N, w, prob))
    plt.xlabel("steps")
    plt.ylabel("position")
    plt.show()
    #plt.savefig('random_walk_1D.png', dpi=1200)

def walk_two_dim() :
    """ gives a visual representation of the two dimensional random walk with N steps """
    global w, N, x0, y0
    walk = np.zeros((N, 2, 10))
    for j in range(w) :
        x, y = x0[j], y0[j]
        walk[0][0][j], walk[0][1][j] = x, y
        for i in range(1, N) :
            t = np.random.rand()
            x += cos(2*pi*t)
            y += sin(2*pi*t)
            walk[i][0][j] = x
            walk[i][1][j] = y
        plt.plot(walk[:, 0, j], walk[:, 1, j], linewidth=0.2)
        #plt.scatter(walk[:,0:,j], walk[:,1:,j], s=0.1, color='black')
    plt.title("2D random walk with {} steps and {} walkers".format(N, w))
    #plt.savefig('random_walk_2D.png', dpi=1200)
    plt.show()


def walk_three_dim() :
    """ gives a visual representation of the three dimensional random walk with N steps """
    global w, N
    walk = np.zeros((N, 3, 10))
    ax = plt.axes(projection='3d')
    for j in range(w) :
        x, y, z = x0[j], y0[j], z0[j]
        walk[0][0][j], walk[0][1][j], walk[0][2][j] = x, y, z
        for i in range(1, N) :
            tht = np.random.rand()
            phi = np.random.rand()
            x += cos(2*pi*phi)*sin(pi*tht)
            y += sin(2*pi*phi)*sin(pi*tht)
            z += cos(pi*tht)
            walk[i][0][j] = x
            walk[i][1][j] = y
            walk[i][2][j] = z
        ax.plot3D(walk[:, 0, j], walk[:, 1, j], walk[:, 2, j], linewidth=0.2)
        #ax.scatter3D(walk[:, 0, j], walk[:, 1, j], walk[:, 2, j], s=0.1, color='black')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("3D random walk with {} steps and {} walkers".format(N, w))
    plt.show()
    
if __name__ == "__main__" :

    startTime = datetime.now()

    # parameters
    N = int(input("Enter the number of steps : "))                                                            # (maximum) number of steps
    w = int(input("Enter the number of walkers : "))
    prob = 0.5 # float(input("Enter the probability to move to the right : "))                                # probability of taking a step to the right
    dim = int(input("Enter the number of dimensions (possible values = 1, 2 or 3) : "))

    x0 = np.linspace(-10*w, 10*w, 10)
    y0 = np.linspace(-7*w, 7*w, 10)
    z0 = np.linspace(-5*w, 5*w, 10)

    if dim == 1 :
        walk_one_dim()
    if dim == 2 :
        walk_two_dim()
    if dim == 3 :
        walk_three_dim()

    endTime = datetime.now()

    print("Execution time : ", endTime - startTime)