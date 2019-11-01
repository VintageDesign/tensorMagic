def tcirc(A):
    '''
    take an n by m by p tensor and slice A from front to back to create an
    np by mp block circ matrix out of the slices

    '''

    dims = len(A)

    n = dims(1)
    m = dims(2)
    p = dims(0)

    mA = np.zeros(n*p, m*p)

    mA[:,0:m] = unfold(A)

    for j in range(1, p):
        mA[:,(j-1)*m+1:j*m] = [mA[(p-2)*n+1:p*n,(j-3)*m+1:(j-2)*m],
                               mA[0:(p-2)*n, (j-3)*m+1:(j-2)*m]]

    return mA
