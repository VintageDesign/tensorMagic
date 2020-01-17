from numpy import linalg
import matplotlib.pyplot as plt
import numpy as np
import math

def plotRecovery(X, sigma):
    '''
    Computes the number of dimensions needed to produce the target data recovery percentage
    using the formula: recoveryPercentage =  (Sum(sigma, 0, i)^2)/froNorm(X)
    Where:
        X:      The data matrix
        sigma:  The vector of sigma values corresponding to the decomposed X
    '''



    # We are doing this one Time Stamp at a Time for now and pulling the Maximum dimension needed

    _, t, _ = sigma.shape
    recoveryPercentage = []
    kVal = 0
    xT = 0

    # Fro norm^2  of a tensor
    for i in np.nditer(X):
        xT += i*i

    while kVal < t:
        kVal += 1
        sigSum = 0

        for i in range(0, kVal):
            temp = linalg.norm(sigma[i, i, :])
            sigSum += temp * temp


        recoveryPercentage.append((sigSum ) / ( xT))
    return recoveryPercentage




def plotRecoveryMatrix(X, sigma):
    t = sigma.shape[0]
    maxK = 0
    recoveryPercentage = []
    kVal = 0
    xT = linalg.norm(X)



    while kVal < t :
        kVal += 1
        sigSum = 0

        for i in range(0, kVal):
            temp = sigma[i]
            sigSum += temp * temp

        recoveryPercentage.append(sigSum / (xT*xT ))

    return recoveryPercentage



