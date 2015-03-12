import numpy as np
from __future__ import division

class Transformations(object):
    """since these transformations are all related, we'll nest them all under a feature norm class"""
    def mean_at_zero(self, arr):
        return np.array([i - np.mean(arr) for i in arr])
        """range where 0 represents the mean"""

    def norm_to_min_zero(self, arr):
        return np.array([i / max(arr) for i in arr])
        """a range from 0 to 1, where """"
    
    def norm_to_absolute_min_zero(self, arr):
        return np.array([(i - min(a)) / (max(a) - min(a)) for i in arr])
        """a range of 0 to 1, where 0 maintains its 0 value"""
    
    def norm_to_neg_pos(self, arr):
        return np.array([(i - np.mean(arr)) / (max(arr) - np.mean(arr)) for i in arr])
        """a range of -1 to 1, where 0 represents the mean"""
    
    def norm_by_std(self, arr):
        return np.array([(i - np.mean(arr)) / np.std(arr) for i in arr])
        """a range where 0 represents the mean, split by standard deviation"""