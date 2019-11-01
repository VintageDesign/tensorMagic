def bcirc(x):
    n1, n2, n3 = X.shape()
    s = np.identity(n3)
    bX = np.zeros(n1*n3, n2*n3)
    for i in range(0, n3):
        S = scipy.linalg.circulant(s(i,:))
        bX += np.kron(S, X[i, :, :])
    return bX
