import numpy as np



class Tensor:
    '''
    Builds multimodal timeseries in relation to Rodgers, Li and Russel's Multi Linear Dynamical
    System
    '''

    def __init__(self, x = 1, y = 1, t = 1, timeSeriesIn = None):
        '''
        Initializes a new tensor of size x x y x t
        '''

        self.timeSeries = np.zeros((t, y, x))
        self.t = t
        self.x = x
        self.y = y


        if timeSeriesIn is not None:
            self.timeSeries = np.asarray(timeSeriesIn)



    def vec(self):
        '''
        Returns the vectorized timeseries
        NOTE must be transposed to use
        '''

        retval = np.zeros(self.t * self.y * self.x)

        # TODO there is probably a way to increase the performance of this but even np implements
        #      their vectorize() as a for loop.
        for sheet in range(0, self.t):
            for xVal in range(0, self.x):
                for yVal in range(0, self.y):
                    # NP is stupid and keeps its arrays in (z, y, x) idexing
                    oneDimIndex = sheet*self.y*self.x + xVal * self.y + yVal
                    retval[oneDimIndex] = self.timeSeries[sheet, yVal, xVal]

        return retval

    def mat(self):
        '''
        Returns the matrix representation of the timeseries, Cols of the matrix each represent a
        single T
        '''
        retval = np.zeros(( self.x * self.y, self.t))

        for sheet in range(0, self.t):
            for xVal in range(0, self.x):
                for yVal in range(0, self.y):
                    # NP is stupid and kee.tolist()ps its arrays in (z, x, y) idexing
                    rowIndex = xVal * self.y + yVal
                    retval[rowIndex, sheet] = self.timeSeries[sheet, yVal, xVal]

        return retval


    def get(self):
        return self.timeSeries



