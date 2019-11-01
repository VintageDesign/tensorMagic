def trans(A):
    '''

    Take an n x m x p tensor A and build the m x n x p tensor transpose of A
    '''



    dims = len(A)

    n = dims(1)
    m = dims(2)
    p = dims(0)

    tA = np.zeros(n, m, p)

    tA[0, :,:] = A[0,:,:]
    # TODO figure out transpose in numpy

    for j in range(p : 1 : -1):
        tA[p-j+2, :, :] = A[j,:,:]
        # TODO transpose again
    return tA
