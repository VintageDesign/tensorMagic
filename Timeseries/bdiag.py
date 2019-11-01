def bdiag(X):
    n1, n2, n3 = X.shape()
    Xbdiag = np.zeros(n1*n3, n2*n3)
    for i in range(1, n3):
        Xbdiag((i-1)*n1+1:i*n1, (i-1)/n2+1:i*n2) = X(i, :, :)
    return Xbdiag
