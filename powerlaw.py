%matplotlib inline
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns

class PowerLaw(object):
    def fit(self, x, y, transform=True):
        """
        returns back the amplitude and index of a powerlaw relationship.
        assumes the data is not already log10 transformed.
        return: [index, amp], also stored on the instance
        """
        if transform:
            x = np.log10(x)
            y = np.log10(y)
        # define our (line) fitting function and error function to optimize on
        fitfunc = lambda p, x: p[0] + p[1] * x
        errfunc = lambda p, x, y: (y - fitfunc(p, x))
        # defines a starting point to optimize from.
        p_init = [1.0, -1.0] 
        out = sp.optimize.leastsq(errfunc, p_init, args=(x, y), full_output=1)
        result = out[0]
        self.index = result[1]
        self.amp = 10.0**result[0]
        return np.array([self.amp, self.index])
    
    def transform(self, x):
        """returns the x-transformed data"""
        return self.amp * (x**self.index)