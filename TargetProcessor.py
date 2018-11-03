import numpy as np

#Calculates the azimuth, altitude, and distance of a given image using the CV camera

class TargetProcessor:
	def __init__(self): 
		self.realWidth = 20 #<--- Declaring all the variables
		self.azi = 0 #<---
		self.alti = 0 #<---
		self.dist = 0 #<---
		self.focalLength = 720 #<---
		self.xOffset = 0#<---
		self.yOffset = 0#<---
	def calculate(self, width, height, centerX, centerY, hsv_img): #calculates the azimuth, distance, altitude
		self.xOffset = hsv_img.shape[0] - centerX #finds the x offset by taking the x center of the image(centerX) and subtracting it by the x center of the target (hsv_img.shape[0])
		self.yOffset = hsv_img.shape[1] - centerY #finds the y offset by taking the y center of the image(centerY) and subtracting it by the y center of the target (hsv_img.shape[1])
		self.dist = (self.focalLength * self.realWidth)/width #calculates distance using the given formula: D = (focalLength * RealWidth)/calculatedWidth (focalLength depends upon the camera)
		self.azi = np.arctan(self.xOffset/self.focalLength) * 180/np.pi #calculates azimuth and converts it to degrees using the given formula: Azi = arctan(xOffset/focalLength) * 180/pi
		self.alti = np.arctan(self.yOffset/self.focalLength) * 180/np.pi #calculates altitude and converts it to degrees using the given formula: Alti = arctan(yOffset/focalLength) * 180/pi
	def getDistance(self): #gets the calculated distance 
		return self.dist
	def getAzimuth(self): #gets the calculated azimuth
		return self.azi
	def getAltitude(self): #gets the calculated altitude
		return self.alti