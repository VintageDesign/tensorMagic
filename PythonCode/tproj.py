def tproj(A,U):
    '''

    Given n x 1 x m tensors A and U, P is the projection of A onto U.
    '''


    n3, n1, n2 = dim(A)
    m3, m1, m2 = dim(U)


    if n2 != 1 or m2 != 1:
        print ("U and A must have a middle dim of 1.")
        raise TypeError

    if n1 != m1 or n3 =! m3:
        print ("Matrix Dimensions Must Agree")
        raise TypeError

    c = tprod(tran(U),A)

    # TODO figure out squeeze
    return squeeze(U) * circ(reshape(tran(c), n3, 1))




