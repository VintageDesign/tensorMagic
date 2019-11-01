def tdiag(A):
    '''
    Compute the tensor diagonalization of tensor A an (n x n x p) tensor.
    '''

    dims = len(A)
    n = dims(1)
    m = dims(2)
    p = dims(0)

    if n != m:
        print('Tensors must have the same size for rows and cols')
        raise TypeError

    mA = tCirc(A)

    # TODO this is the matlab code for this section, I think there is probably
    #      another library I need to use
    F  = kron(fft(eye(n,n)), eye(n,n))
    iF = kron(ifft(eye(n,n)), eye(n,n))

    D = F*mA*iF

    DX    = zeroes (n*p, n*p)
    DXinv = zeroes (n*p, n*p)
    DL    = zeroes (n*p, n*p)

    for i in rang(0,p):
        DX((i-1)*n+1:n+1, (i-1)*n+1:i*n), DL((i-1)*n+1:i*n,(i-1)*n+1:i*n) = \
                eig(D((i-1)*n+1:i*n, (i-1)*n+1:i*n))

    XX = iF*DX*F
    LL = iF*DL*F
    XXinv = iF*DXinv*F

    X = fold(XX, n, m, p)
    L = fold(LL, n, m, p)
    Xinv = Fold(XXinv, n, m, p)

    return X, L, Xinv

