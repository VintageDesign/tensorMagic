def tERecovEst(X, Uest, mu):
    '''
    Compute the energy of a tensor recovered by a given subspace
      Usage: rho = Erecov(X,S)
     Inputs: X-Tensor, S- singular tuples of the tensor
    Outputs: The energy recovered
    '''
    rho = []

    NX = fronorm(X)^2

    p, n, m = len(Uest)

    RT = fronorm(tprod(tran(Uest(:, :, 0)), X))^2

    rho.append(RT)

    for i in range(1:m):
        RT = RT + fronorm(tprod(tran(Uest(:,:,i)),X))^2
        rho.append(RT)
        if rho(i)/NX > mu:
            break

    rho = rho ./ NX # TODO syntax
    p = i

    return rho, p

