import cv2
import numpy as np

class TargetDetector(object):
    """Processes image for target contour"""
    def __init__(self, img):
        self.img = img
        #convert to hsv for contours
        self.img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
    #find threshold image
    def threshold(self):
       THRESHOLD_MIN = np.array([100, 70, 70], np.uint8)
       THRESHOLD_MAX = np.array([255, 255, 255], np.uint8)
       #thresholded image for contours
       self.thresh = cv2.inRange(self.img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)
    #find contours
    def contours(self):
        img_thresh, self.contours, heirarchy = cv2.findContours(self.thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #find contours for the target
    def filterContours(self):
        #list of coordinates
        self.coordinates = []
        for cont in self.contours:
            epsilon = 0.01 * cv2.arcLength(cont, True)
            #find polygons
            approx = cv2.approxPolyDP(cont, epsilon, True)
            #plus shape has 12 sides
            if len(approx) == 12 and cv2.contourArea(approx) > 100:
                cv2.drawContours(self.img, contours, count, (255, 0, 0), 4)
                result.append(approx)
            count += 1
    #return coordinates of target contour
    def getContour(self):
        return self.coordinates