import numpy as np
import cv2
class TargetDetector:
    lightblue = (255, 221, 0)
    contours = None
    index = None
    corners = None

    def __init__(self):
        pass

    def threshold(self,min,max,frame):                          # method that converts frame to HSV and then returns new frame of thresholded values
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv, min, max)
        return thresh

    def contours(self,threshold):                               # method that finds and sets the contours to the variable contours for later usage
        HSV,self.contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    def filterContours(self):
        for c in range(len(self.contours)):                     # method that iterates through each contour in the contours array and filters them by number and size
            epsilon = 0.1 * cv2.arcLength(self.contours[c],True)
            approx = cv2.approxPolyDP(self.contours[c],epsilon, True)
            if(len(approx)==4 and cv2.contourArea(approx)>100):
                self.index = c
                self.corners = approx

    def getContours(self):                                      # getter method that returns the contours array, index of significant contour, and the corners array
        return self.contours,self.index,self.corners
