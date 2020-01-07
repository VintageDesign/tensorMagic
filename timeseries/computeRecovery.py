from numpy import linalg
import numpy as np
import math

def getRecoveryValue(X, sigma, targetAmount = .9):
    '''
    Computes the number of dimensions needed to produce the target data recovery percentage
    using the formula: recoveryPercentage =  (Sum(sigma, 0, i)^2)/froNorm(X)
    Where:
        X:      The data matrix
        sigma:  The vector of sigma values corresponding to the decomposed X
    '''



    # We are doing this one Time Stamp at a Time for now and pulling the Maximum dimension needed

    _, _, t = X.shape


    maxK = 0



   # Inital values
    recoveryPercentage = 0.0
    kVal = 0


    xT = 0
    for i in np.nditer(X):
        xT += i*i


    while recoveryPercentage < targetAmount:
        kVal += 1
        sigSum = 0

        for i in range(0, kVal):
            temp = linalg.norm(sigma[i, i, :])
            sigSum += temp * temp


        recoveryPercentage =   (sigSum ) / ( xT)



    if kVal > maxK:
         maxK = kVal




    return maxK
