import t_svd
import L_svd
import scipy
import time
import numpy as np
import numpy.linalg as linalg
import os.path
from matplotlib.pylab import plt #load plot library


from computeRecovery import getRecoveryValue, getRecoveryValueMatrix
from plotRecoveryTensor import plotRecovery, plotRecoveryMatrix
filename = "day2"
start = time.time()

# Save the SVD output cause this takes for ever to run
if  not os.path.exists(filename + "_Theta.npz") or not os.path.exists(filename + "_D.npz"):
    calc_time_start = time.time()
    print("Recalulating T_Svd")
    tensor = np.load(filename+'.npz')
    tensor = tensor['arr_0']
    tensor = np.swapaxes(tensor, 1, 2)
    theta, D = t_svd.t_svd(tensor)
    calc_time_stop = time.time()
    print("T_SVD Calc Time:", str((calc_time_stop - calc_time_start) / 60), "minutes")
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
    calc_time_start = time.time()
    sigma, D = L_svd.L_svd(tensor, 'dct')
    calc_time_stop = time.time()
    print("DCT_SVD Calc Time:", str((calc_time_stop - calc_time_start) / 60), "minutes")

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

if  not os.path.exists(filename + "_Theta_hwt.npz") or not os.path.exists(filename + "_D_hwt.npz"):
    print("Recalulating hwt_Svd")
    tensor = np.pad(tensor, ((0,0),(0,0),(0, 2048 - tensor.shape[2])), 'constant', constant_values=(0, 0))
    calc_time_start = time.time()
    sigma, D = L_svd.L_svd(tensor, 'hwt')
    calc_time_stop = time.time()
    print("DCT_SVD Calc Time:", str((calc_time_stop - calc_time_start) / 60), "minutes")

    #np.savez_compressed(filename + '_U_hwt.npz', U)
    np.savez_compressed(filename + '_Theta_hwt.npz', sigma)
    np.savez_compressed(filename + '_D_hwt.npz', D)

else:
    #tensor = np.load(filename + '_U_hwt.npz')
    #U = tensor['arr_0']

    tensor = np.load(filename + '_Theta_hwt.npz')
    sigma= tensor['arr_0']

    tensor = np.load(filename + '_D_hwt.npz')
    D = tensor['arr_0']

    tensor = np.load(filename + '.npz')
    tensor = tensor['arr_0']
    tensor = np.swapaxes(tensor, 1, 2)

print("HWT_svd:", getRecoveryValue(tensor, sigma))
hwtSvdResults = plotRecovery(tensor, sigma)

# Now the same math, but in 2D

x, z, y = tensor.shape

matrix = np.zeros((x*y, z))

for i in range(0, z):
    matrix[:, i] = tensor[:, i, :].flatten()


Sigmat = linalg.svd(matrix, full_matrices=True, compute_uv=False)
print(Sigmat.shape)
print("Standard 2d SVD:", getRecoveryValueMatrix(matrix, Sigmat))
svdResults = plotRecoveryMatrix(matrix, Sigmat)
end = time.time()
print("This little manuver just cost us", (end-start) /60, "minutes")

plt.plot(tSvdResults, label='T_SVD')
plt.plot(DCTSvdResults, label='DCT_SVD')
plt.plot(hwtSvdResults, label='HWT_SVD')
plt.plot(svdResults, label='Matrix SVD')
plt.legend()
plt.xlabel('Dimensions')
plt.ylabel('Energy Recovery (%)')
plt.show()
