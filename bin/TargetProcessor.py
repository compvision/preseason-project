import math

class TargetProcessor:
    d  = 0
    az = 0
    al = 0

    def __init__(self):
        pass

    def calculate(self,f,w,iw,x,h):                     # method that calculates Distance, Azimuth, and Altitude
        self.d = (f*w)/iw
        self.az = math.atan(x/f)*180/math.pi
        self.al = math.atan(h/f)*180/math.pi

    def getDistance(self):                              # getter method that returns distance rounded to two decimal places
        return round(self.d,2)

    def getAltitude(self):                              # getter method that returns altitude rounded to four decimal places
        return round(self.al,4)

    def getAzimuth(self):                               # getter method that returns azimuth rounded to four decimal places
        return round(self.az,4)
