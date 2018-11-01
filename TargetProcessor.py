import numpy as np

class TargetProcessor(object):
    """Calculates distance, azimuth, and altitude"""
    def __init__(self, img, contours):
        #set focal length and target size in cm
        self.focal = 700
        self.width, self.height = (50, 25)
    #return distance
    def distance(self, xmin, xmax):
        return (self.focal * self.width)/(xmax - xmin)
    #return azimuth
    def azimuth(self, center, img_center):
        return np.rad2deg(np.arctan2(center[0] - img_center[0], self.focal))
    #return altitude
    def altitude(self, center, img_center):
        return np.rad2deg(np.arctan2(-(center[1] - img_center[1]), self.focal))