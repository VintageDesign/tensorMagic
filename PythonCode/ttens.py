def ttens(A,B):
    '''
    Performs tensor multiplication on A (n x m x q) and B (m x p x q) as defined
    by Kilmer, Martin, and Perrone.
    The retval is C with dimensions n x p x q
    '''


    dimsA = len(A)
    dimsB = len(B)

    if len(dimsB) == 2:
        dimsB = [dimsB(0), 1, dimsB(1)]

    n = dimsA(1)
    m = dimsA(2)
    q = dimsA(0)
    p = dimsB(2)

    if dimsB(1) != m or dimsB(0) != q:
        print("Incorect Tensor Dimensions!")
        raise TypeError

    C = fold(tcirc(A)*unfold(B), n, p, q)

    return C
