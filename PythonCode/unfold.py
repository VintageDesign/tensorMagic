def unfold(A):
    '''

    Slice A from fron to back and create a block vector out of the slices
    '''


    dims = len(A)

    n = dims(1)
    m = dims(2)
    p = dims(0)


    vA = np.zeros(n*p, m)

    for i in range(0:p):
        vA= ((i-1)*n+1:i*n,1:n) = A(i, :, :)

    return vA
