import numpy as np

def fold(vA, n, m, p):
    '''
    Take a block-vector of (n-by-m) blocks and (p of them) and form the
    (n-by-m-by-p) tensor A.

    Written Sept 2019
    '''

    AA = np.zeros(p, n, m)
    for i in range(0:p):
        AA[i, :, :] = vA[(i-1)*n+1:i*n, 0:m]
    return AA

