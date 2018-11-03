import math


class TargetProcessor:

    distance = None
    azimuth = None
    altitude = None
    """Defining Global variables"""

    def __init__(self):
        pass

    """Simple function which turns radians to degrees"""
    """:return degrees"""
    def radiansToDegrees(self, radians):
        return radians * (180 / math.pi)

    """calculates azimith, distance, and altitude with given 
parameters"""
    def calculate(self, focalLength, actualWidth, imageWidth, image, 
targetCenterX, targetCenterY):

        """Finding the center of the image"""
        imgCenterY = image.shape[0] / 2
        imgCenterX = image.shape[1] / 2

        """Using focal length and distance to get distance and storing 
it in global variable"""
        self.distance = (focalLength * actualWidth) / imageWidth

        """Using parameters and center of target to determine values for 
next calculation"""
        H_azimuth = targetCenterX - imgCenterX
        H_altitude = targetCenterY - imgCenterY

        """With above values, calculate and store azimuth and 
altitude"""
        self.azimuth = self.radiansToDegrees(math.atan(float(H_azimuth) 
/ focalLength))
        self.altitude = 
self.radiansToDegrees(math.atan(float(H_altitude) / focalLength))

    """:returns distance"""
    def getDistance(self):
        return self.distance

    """:returns azimuth"""
    def getAzimuth(self):
        return self.azimuth

    """:returns altitude"""
    def getAltitude(self):
        return self.altitude

