from tensor import Tensor
import numpy as np

testIn = np.zeros((3, 3, 3))
testIn[0, 1, 1] = 1
testIn[1, 1, 1] = 2
testIn[2, 1, 1] = 3

print(testIn)

test = Tensor(testIn, 3, 3, 3)

print(test.circ())

