import numpy as np
from scipy import linalg


class Tensor:
    def __init__(self, threeDimArray, xSize, ySize, zSize):
        self.tensorSize = (xSize, ySize, zSize)
        self.tensor = threeDimArray

    def circ(self):
        return linalg.circulant(self.tensor)





