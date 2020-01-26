import scipy
import time
import numpy as np
import numpy.linalg as linalg
import os.path
from matplotlib.pylab import plt #load plot library


#from computeRecovery import getRecoveryValue, getRecoveryValueMatrix
#from plotRecoveryTensor import plotRecovery, plotRecoveryMatrix
filename = "day2"
start = time.time()

# Save the SVD output cause this takes for ever to run
U_x = []
U_y = []

t_size = 40
for t in range(0, t_size):
    tensor = np.load(filename+'.npz')
    tensor = tensor['arr_0']
    matrix = tensor[:, :, t]
    tensor = None
    U, sigma, V = linalg.svd(matrix)

    U_x.append(U[0, :])
    U_y.append(U[1, :])




plt.plot(U_x[1], U_y[1], label='Matrix SVD')
plt.show()
