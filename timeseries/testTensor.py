import t_svd
import L_svd
import scipy
import numpy as np
import numpy.linalg as linalg
import os.path
from matplotlib.pylab import plt #load plot library


from computeRecovery import getRecoveryValue, getRecoveryValueMatrix
from plotRecoveryTensor import plotRecovery, plotRecoveryMatrix
filename = "boats"


# Save the SVD output cause this takes for ever to run
if  not os.path.exists(filename + "_Theta.npz") or not os.path.exists(filename + "_D.npz"):
    print("Recalulating T_Svd")
    tensor = np.load(filename+'.npz')
    tensor = tensor['arr_0']
    tensor = np.swapaxes(tensor, 1, 2)
    print(tensor.shape)
    theta, D = t_svd.t_svd(tensor)

    #np.savez_compressed(filename + '_U.npz', U)
    np.savez_compressed(filename + '_Theta.npz', theta)
    np.savez_compressed(filename + '_D.npz', D)

else:
    #tensor = np.load(filename + '_U.npz')
    #U = tensor['arr_0']

    tensor = np.load(filename + '_Theta.npz')
    theta= tensor['arr_0']

    tensor = np.load(filename + '_D.npz')
    D = tensor['arr_0']

    tensor = np.load(filename + '.npz')
    tensor = tensor['arr_0']
    tensor = np.swapaxes(tensor, 1, 2)





print("T_svd:", getRecoveryValue(tensor, theta))
tSvdResults = plotRecovery(tensor, theta)

if  not os.path.exists(filename + "_Theta_dct.npz") or not os.path.exists(filename + "_D_dct.npz"):
    print("Recalulating Cosine_Svd")
    sigma, D = L_svd.L_svd(tensor, 'dct')

    #np.savez_compressed(filename + '_U_dct.npz', U)
    np.savez_compressed(filename + '_Theta_dct.npz', sigma)
    np.savez_compressed(filename + '_D_dct.npz', D)

else:
    #tensor = np.load(filename + '_U_dct.npz')
    #U = tensor['arr_0']

    tensor = np.load(filename + '_Theta_dct.npz')
    sigma= tensor['arr_0']

    tensor = np.load(filename + '_D_dct.npz')
    D = tensor['arr_0']

    tensor = np.load(filename + '.npz')
    tensor = tensor['arr_0']
    tensor = np.swapaxes(tensor, 1, 2)

print("DCT_svd:", getRecoveryValue(tensor, sigma))
DCTSvdResults = plotRecovery(tensor, sigma)

if  not os.path.exists(filename + "_Theta_hilbert.npz") or not os.path.exists(filename + "_D_hilbert.npz"):
    print("Recalulating Hilbert_Svd")
    sigma, D = L_svd.L_svd(tensor, 'hilbert')

    #np.savez_compressed(filename + '_U_hilbert.npz', U)
    np.savez_compressed(filename + '_Theta_hilbert.npz', sigma)
    np.savez_compressed(filename + '_D_hilbert.npz', D)

else:
    #tensor = np.load(filename + '_U_hilbert.npz')
    #U = tensor['arr_0']

    tensor = np.load(filename + '_Theta_hilbert.npz')
    sigma= tensor['arr_0']

    tensor = np.load(filename + '_D_hilbert.npz')
    D = tensor['arr_0']

    tensor = np.load(filename + '.npz')
    tensor = tensor['arr_0']
    tensor = np.swapaxes(tensor, 1, 2)

print("Hilbert_svd:", getRecoveryValue(tensor, sigma))
HilbertSvdResults = plotRecovery(tensor, sigma)

# Now the same math, but in 2D

print("Tensor Size:", tensor.shape)
x, z, y = tensor.shape

matrix = np.zeros((x*y, z))
print("Matrix size:", matrix.shape)

for i in range(0, z):
    matrix[:, i] = tensor[:, i, :].flatten()


Sigmat = linalg.svd(matrix, full_matrices=True, compute_uv=False)
print(Sigmat.shape)
print("Standard 2d SVD:", getRecoveryValueMatrix(matrix, Sigmat))
svdResults = plotRecoveryMatrix(matrix, Sigmat)

plt.plot(tSvdResults, label='T_SVD')
plt.plot(DCTSvdResults, label='DCT_SVD')
plt.plot(HilbertSvdResults, label='Hilbert_SVD')
plt.plot(svdResults, label='Matrix SVD')
plt.legend()
plt.show()
