import numpy as np


class tensor:
    def __init__(self, threeDimArray, xSize, ySize, zSize):
        self.tensorSize = (xSize, ySize, zSize)
        self.tensor = threeDimArray

    def circularize(self):



