from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor
from Target import Target
import cv2

#Main.py runs the entire program, integrating all the other classes

cameraID = 0

#Intializaing all the objects
cam = cv2.VideoCapture(cameraID) 
detector = TargetDetector()
target = Target()
processor = TargetProcessor()

while(True):
	ret, frame = cam.read() #Gets the image from the camera (frame) and whether or not it receives a proper image (ret: returns true or false)
	if not ret:	
		continue
	detector.threshold(frame) #threshold the originial image, the live camera frame in this case
	detector.contours(detector.getThreshed(), frame) #Contour the image using the threshed image
	HSV = detector.getHSV()									#<--- Gets variables from different classes, mainly for parameters in the processor
	height = target.getHeight(detector.getApprox())			#<---
	width = target.getWidth(detector.getApprox())			#<---
	centerX = target.getCenterX()							#<---	
	centerY = target.getCenterY()							#<---
	processor.calculate(width, height, centerX, centerY, HSV) #Calculating azimuth, altitude, and distance using the width, height, centerX, centerY, and the HSV image
	dist = processor.getDistance() #Receive the distance calculated by processor.calculate()
	azi = processor.getAzimuth() #Receive the azimuth calculated by processor.calculate()
	alti = processor.getAltitude() #Receive the altitude calculated by processor.calculate()
	print("Distance: " + str(dist)) #Print distance
	print("Azimuth: " + str(azi)) #Print azimuth
	print("Altitude: " + str(alti)) #Print altitude
	if (cv2.waitKey(10) == 27): #When escape is pressed, stop the program (from looping)
		break