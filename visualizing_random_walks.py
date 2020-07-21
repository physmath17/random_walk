import numpy as np
from numpy import pi, sin, cos
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def walk_one_dim() : 
    """ gives a visual representation of the one dimensional random walk with N steps """
    global N, prob
    walk = np.array([np.float64(x) for x in range(0)])
    s = 0
    for i in range(N) :                             # loops through the number of steps
        r = np.random.rand()                        # random number to decide whether the walker goes left or right
        s += 1*(r<prob) + (-1)*(r>prob)             # describes the walk
        walk = np.append(walk, [s])
    steps = np.linspace(0, N, N)
<<<<<<< HEAD
    plt.scatter(steps, walk, alpha=0.5, s=0.1, color='blue')
    plt.title("1D random walk with {} steps".format(N))
    plt.xlabel("steps")
    plt.ylabel("position")
    plt.show()
    #plt.savefig('random_walk_1D.png', dpi=1200)
=======
    plt.scatter(steps, walk, alpha=0.2, s=0.1, color='red')
    plt.savefig('random_walk_1D.png', dpi=1200)

    
>>>>>>> 90c9615152b9c2a41ccb58d7d8f8f01b64b930b2

def walk_two_dim() :
    """ gives a visual representation of the two dimensional random walk with N steps """
    global N
    walk = np.zeros((N,2))
    x, y = 0, 0
    for i in range(1, N) :
        t = np.random.rand()
        x += cos(2*pi*t)
        y += sin(2*pi*t)
        walk[i][0] = x
        walk[i][1] = y
<<<<<<< HEAD
    plt.plot(walk[:,0], walk[:,1], linewidth=0.2, color='blue')
    plt.scatter(walk[:,0], walk[:,1], s=0.1, color='black')
    plt.title("2D random walk with {} steps".format(N))
    #plt.savefig('random_walk_2D.png', dpi=1200)
    plt.show()

=======
    plt.plot(walk[:,0], walk[:,1], linewidth=0.2, color='cyan')
    plt.scatter(walk[:,0], walk[:,1], s=0.1, color='black')
    plt.savefig('random_walk_2D.png', dpi=1200)
>>>>>>> 90c9615152b9c2a41ccb58d7d8f8f01b64b930b2

def walk_three_dim() :
    """ gives a visual representation of the three dimensional random walk with N steps """
    global N
    walk = np.zeros((N,3))
    x, y, z = 0, 0, 0
    for i in range(1, N) :
        tht = np.random.rand()
        phi = np.random.rand()
        x += cos(2*pi*phi)*sin(pi*tht)
        y += sin(2*pi*phi)*sin(pi*tht)
        z += cos(pi*tht)
        walk[i][0] = x
        walk[i][1] = y
        walk[i][2] = z
    ax = plt.axes(projection='3d')
    ax.plot3D(walk[:,0], walk[:,1], walk[:,2], linewidth=0.2, color='blue')
    #ax.scatter3D(walk[:,0], walk[:,1], walk[:,2], s=0.1, color='black')
<<<<<<< HEAD
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("3D random walk with {} steps".format(N))
=======
>>>>>>> 90c9615152b9c2a41ccb58d7d8f8f01b64b930b2
    plt.show()
    

if __name__ == "__main__" :
    # parameters
<<<<<<< HEAD
    N = int(input("Enter the number of steps : "))                                                            # (maximum) number of steps
=======
    N = int(input("Enter the (maximum) number of steps : "))                                                            # (maximum) number of steps
>>>>>>> 90c9615152b9c2a41ccb58d7d8f8f01b64b930b2
    prob = 0.5 # float(input("Enter the probability to move to the right : "))                                          # probability of taking a step to the right
    dim = int(input("Enter the number of dimensions (possible values = 1, 2 or 3) : "))
    if dim == 1 :
        walk_one_dim()
    if dim == 2 :
        walk_two_dim()
    if dim == 3 :
        walk_three_dim()