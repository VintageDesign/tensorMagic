import pycuda.autoinit
import scipy
import pycuda.gpuarray as gpuarray
import time
import numpy as np
import skcuda.linalg as linalg
import os.path
from matplotlib.pylab import plt #load plot library

linalg.init()

#from computeRecovery import getRecoveryValue, getRecoveryValueMatrix
#from plotRecoveryTensor import plotRecovery, plotRecoveryMatrix
filename = "day2_little"
start = time.time()

# Save the SVD output cause this takes for ever to run
U_x = []
U_y = []

tensor = np.load(filename+'.npz')
tensor = tensor['arr_0']
t_size = 1
for t in range(0, t_size):
    print("Starting", t)
    matrix = np.asarray(tensor[:, :, t], np.float32)
    print(matrix[0:10, 0:10])
    matGpu = gpuarray.to_gpu(matrix)
    U, _,  V = linalg.svd(matGpu, 'S', 'S')
    print(U.get()[:,0])
    #U_x.append(U.get()[:, 0])
    #U_y.append(U.get()[:, 1])

    U_x.append(V.get()[0, :])
    U_y.append(V.get()[1, :])



end = time.time()
print("Time elapsed:", str((end - start)/60), "minutes")

plt.scatter(U_x[0], U_y[0])
plt.show()
