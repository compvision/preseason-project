import cv2
from TargetDetector import TargetDetector
from Target import Target
from TargetProcessor import TargetProcessor

class Main(object):
    """Runs everything"""
    def __init__(self, img):
        self.img = img
        self.detect = TargetDetector(self.img)
        self.detect.threshold()
        self.target = Target(self.img, self.detect.findRect())
        self.processor = TargetProcessor(self.img, self.detect.findRect())
    #show image with contours and the threshold image
    def display(self):
        cv2.imshow("image", self.detect.img)
        cv2.imshow("thresh", self.detect.thresh)
    #return distance
    def distance(self):
        return self.processor.distance(self.target.xmin, self.target.xmax)
    #return azimuth
    def azimuth(self):
        return self.processor.azimuth(self.target.center(), self.target.img_center())
    #return altitude
    def altitude(self):
        return self.processor.altitude(self.target.center(), self.target.img_center())