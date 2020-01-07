from numpy import linalg

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


    for i in range(0, 5):
        print(sigma[i, i, :])

    for tIndex in range(0, t):
       # Inital values
       recoveryPercentage = 0.0
       kVal = 0

       sigmaT = sigma[:, :, tIndex]
       xT     = linalg.norm(X[:, :, tIndex], ord='fro')
       print("t: ", tIndex)
       print("Fro X^2: ", xT * xT)
       print("Max K: ", maxK)



       while recoveryPercentage < targetAmount:
           kVal += 1
           sigSum = 0

           for i in range(0, kVal):
               sigSum += sigmaT[kVal, kVal] * sigmaT[kVal, kVal]


           recoveryPercentage =   (sigSum ) / (xT * xT)
       print("Sigma Sum: ",  sigSum)
       print("ER: ",recoveryPercentage, "\n")



       if kVal > maxK:
            maxK = kVal




    return maxK
