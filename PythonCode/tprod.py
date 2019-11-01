def tprod(A, B):
    '''
    compute the tensor - tensor product using FFTs
    A is an n1 x n2 x n3
    B is an na x n4 x nb
    Output is n1 x n4 x n3

    Follows Multiplication defined by Kilmer, Martin, and Perrone

    '''


    n3, n1, n2 = len(A)

    nb, na, n4 = len(B)

    C = np.zeros((n3, n1, n4))

    if n3 != nb or n2 != na:
        print("Matrix Dimensions Must Agree")
        raise TypeError

    D = fft(A, [], 3) # TODO Fourier Transform
    Bhat = fft(B, [], 3)

    for i in range(0, n3):
        C[i, :, :] = D[i,:,:] * Bhat[i, :, :]

    return ifft(C, [], 3)
