import t_svd
import scipy
import numpy as np
import os.path

from computeRecovery import getRecoveryValue


# Save the SVD output cause this takes for ever to run
if not os.path.exists("day_2_U.npz") or not os.path.exists("day_2_Theta.npz") or not os.path.exists("day_2_D.npz"):
    tensor = np.load('day_2_tensor.npz')
    tensor = tensor['arr_0']
    tensor = np.swapaxes(tensor, 1, 2)
    print(tensor.shape)
    U, theta, D = t_svd.t_svd(tensor)

    np.savez_compressed('day_2_U.npz', U)
    np.savez_compressed('day_2_Theta.npz', theta)
    np.savez_compressed('day_2_D.npz', D)

else:
    tensor = np.load('day_2_U.npz')
    U = tensor['arr_0']

    tensor = np.load('day_2_Theta.npz')
    theta= tensor['arr_0']

    tensor = np.load('day_2_D.npz')
    D = tensor['arr_0']

    tensor = np.load('day_2_tensor.npz')
    tensor = tensor['arr_0']


print("U: ", U.shape)
print("Sigma: ", theta.shape)
print("D: ", D.shape)




print(getRecoveryValue(tensor, theta))


# Assuming that the SVD I stole actually does what it is supposed to
#x, y, t = theta.shape
#disconnect = {}

#for tIter in range(0, t):
#    disconnect[tIter] = 0
#    for xIter in range (0, x):
#        if theta[xIter, xIter, tIter] == 0:
#            disconnect[tIter] += 1


#for tIter in range(0, t):
#    zeroCount = disconnect[tIter]
#    if zeroCount > 1:
#        print("Minute", tIter, "is disconnected")





