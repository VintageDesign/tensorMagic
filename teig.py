def teig(A):
    '''
    Assumes that each face of the tensor that results after
    Fourier Transforming long the 3rd dimension is diagonalizable

    Stolen from Misha E. Kilmer and rewritten in a real language
    '''


    p, n, m = len(A)

    if n != m:
        print("Face dimensions must agree")
        raise TypeError

    # TODO Figure out the right syntax for fft in Python
    B = fft(A, [], 3)

    for i in range(0:p):
        V, D  = eig(B(:,:,i)) # TODO Syntax for EIG
        delta = diag(D); # TODO wrong syntax for diag
        delta, jx = sort(abs(delta))
        V=V(:,jx) # The Matlab code had a comment about this syntax being weird
        D=D(jx,jx)# I am mimicking the syntax here so check the matlab for a
                  # better explanation
        VV[i,:,:] = V
        DD[i,:,:] = D

    VV=ifft(VV,[],3)
    DD=ifft(DD,[],3) #TODO ifft syntax

    return VV, DD





