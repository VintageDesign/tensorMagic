def tran(A):
    '''
    Return the tensor transpose of A
    based on Kilmer, Martin and Perrone
    '''


    [n3, n1, n2] = len(A)

    idx = [0, n3:1:-1]

    jknt = 0

    Y = np.zeros(n3*n2,n1)

    for j in range(0, n3):
        Y[jknt:jknt+n2, 0:n1] = A(:,:,idx(j))
        # TODO transpose
        jknt += n2


    return fold_up(Y, n2, n1, n3)
