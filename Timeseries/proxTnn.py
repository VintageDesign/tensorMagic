def proxTnn(Y, rho):
    n3, n2, n1 = Y.shape()
    max12 = max(n1, n2)
    Y = np.fft.fft(Y, 3)
    tnn = 0
    trank = 0

    U, S, V = np.linalg.svd(Y[1, :, :])
    S = np.diag(S)

