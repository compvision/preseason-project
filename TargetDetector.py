import numpy as np
import cv2

#TargetDetector.py thresholds a given image, puts contours on a given threshed image, and returns threshed images, contoured images, 
#the approx value(which contains all the contour points), and the HSV image

class TargetDetector:
	def __init__(self):
		self.contr = None #<--- Declare all the variables
		self.thresh = None #<---
		self.aprx = None #<---
		self.hsv_img = None #<---
	def threshold(self, originalImage): #thresholds a given original image (the frame in this program)
		self.hsv_img = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV) #converts the RGB image to an HSV image in which it can be threshholded 
		THRESHOLD_MIN = np.array([0,0,0], np.uint8) #initializes the minimum threshold values
		THRESHOLD_MAX = np.array([255,100,100], np.uint8) #initializes the maximum threshold values
		self.thresh = cv2.inRange(self.hsv_img, THRESHOLD_MIN, THRESHOLD_MAX) #creates a thresholded image, using the HSV image, the minimum threshold values, and the maximum threshold values
		cv2.imshow("THRESHED IMAGE", self.thresh) #Displays the thresholded image on the screen
	def contours(self, thresholdedImg, originalImg): #Contours a given threshed image and draws the contours on a given original image
		count = -1 
		images, contours, hierarchy = cv2.findContours(thresholdedImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #gets the contour
		for cont in contours: #loops through each contour
			count = count + 1
			approx = cv2.approxPolyDP(cont, 0.1*cv2.arcLength(cont, True), True) #storing an array of points of the contour that is being looped
			if (cv2.contourArea(approx) > 1000 and len(approx) == 4): #Checking if the contour detected is greater than 1000 area and has 4 sides (for filtering)
				cv2.drawContours(originalImg, contours, count, (255,10,255), 5) #draws the contour
		cv2.imshow("CONTOURS", originalImg) #Displays the contour on the screen
		self.contr = originalImg #initializing the contour variable being returned to the image with contours drawin on it
		self.aprx = approx #initializing the approx variable being returned 
	def getThreshed(self): #gets the original image thresholded
		return self.thresh
	def getContour(self): #gets the original image with contours drawn on it
		return self.contr
	def getApprox(self): #gets the approx array
		return self.aprx
	def getHSV(self): #gets the HSV image
		return self.hsv_img
		