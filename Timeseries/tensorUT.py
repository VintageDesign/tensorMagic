import unittest
from tensor import Tensor
import numpy as np

class tensorUnitTests (unittest.TestCase):

    def testGet(self):
        testTensor = Tensor( t = 1, x = 1, y = 1)

        self.assertEqual([[0]], testTensor.get())

    def testvec(self):
        testtensor = Tensor( t = 2, x = 3, y = 2, timeSeriesIn = [[[1, 3, 5],[ 2, 4, 6]],[[7, 9, 11], [8, 10, 12]]])

        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], testtensor.vec().tolist())

    def testmat(self):
        testtensor = Tensor( t = 2, x = 3, y = 2, timeSeriesIn = [[[1, 3, 5],[ 2, 4, 6]],[[7, 9, 11], [8, 10, 12]]])

        self.assertListEqual(np.array([[ 1.,  7.],[ 2.,  8.],[ 3.,  9.],[ 4., 10.],[ 5., 11.],[ 6., 12.]]).tolist(), testtensor.mat().tolist())

