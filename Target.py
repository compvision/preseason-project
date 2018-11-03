import cv2
import numpy as np

#Target.py gets the information from the target, such as height, width, and centerX, centerY

class Target:
	def __init__(self): 
		self.height = 0 #<--- Declare all the variables
		self.width = 0 #<---
		self.centerX = 0 #<---
		self.centerY = 0 #<---
		self.maxX = 0 #<---
		self.minX = 1000 #<---
		self.maxY = 0 #<---
		self.minY = 1000 #<---
	def getHeight(self, approx): #calculates the height, using the approx variable (which gives each point of the contour), and it returns the calculated height
		for i in approx: #looping through each point in approx
			if (i[0][1] < self.minY): #checking if there is a y value less than the minimum y
				self.minY = i[0][1] #if so, set the minimum y equal to that
			if (i[0][1] > self.maxY): #checking if there is a y value greater than the maximum y
				self.maxY = i[0][1] #if so, set the maximum x equal to that
		self.height = self.maxY - self.minY #calculating the height by subtracting the minimum y by the maximum y
		return self.height #returning the calculated height
	def getWidth(self, approx): #calculates the width, using the approx variable, and it returs the calculated width
		for i in approx: #looping through each point in approx
			if (i[0][0] < self.minX): #checking if there is an x value less than the minimum x value
				self.minX = i[0][0] #if so, set the minimum x value equal to that
			if (i[0][0] > self.maxX): #checking of there is an x value greater than the maximum x value
				self.maxX = i[0][0] #if so, set the maxximum x value equal to that
		self.width = self.maxX - self.minX #calculating the width by subtracting the minimum x by the maximum x
		return self.width #returns the width
	def getCenterX(self): #calculates and returns the centerX
		self.centerX = (self.maxX + self.minX)/2 #taking the average of the maxX and minX (which are calculated using approx in getWidth) to calculate the centerX
		return self.centerX #returns the centerX
	def getCenterY(self): #calculates and returns the centerY 
		self.centerY = (self.maxY + self.minY)/2 #taking the average of the maxY and minY (which are calculated using approx in getHeight) to calculate the centerY
		return self.centerY #returns the centerY