def fold_up(A, n1, n2, n3):
    '''
    fold the array in A back up to a tensor
    Input should be n1*n3 x n2

    '''


    k = 0

    y = np.zeros(n3, n1, n2)

    for i in range(0, n3):
        y[i, :, :] = A[k+1:k+n1, 0:n2)
        k += 1


    return y
