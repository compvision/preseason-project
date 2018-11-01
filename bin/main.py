from Target import Target
from TargetDetector import TargetDetector as Detector
from TargetProcessor import TargetProcessor as Processor
import numpy as np
import cv2

actualWidth = int(input("\nEnter actual target width: "))                       # allowing users to input the actual width and thresholds
minValues = input("Enter min threshold values with spaces separating them(ex. H S V): ")
maxValues = input("Enter max threshold values with spaces separating them(ex. H S V): ")
hmin,smin,vmin = minValues.split()
hmax,smax,vmax = maxValues.split()
minThreshold = np.array([int(hmin),int(smin),int(vmin)], np.uint8)
maxThreshold = np.array([int(hmax),int(smax),int(vmax)], np.uint8)
lightblue = (255, 221, 0)
focalLength = 700
degrees = u'\N{DEGREE SIGN}'
centimeters = " cm"

def displayValues():                                                            # method that prints out the values in a nice format
    print("\n"+"Distance = " + str(proc.getDistance())+centimeters)
    print("Azimuth = " + str(proc.getAzimuth())+degrees)
    print("Angle of Altitude = "+ str(proc.getAltitude())+degrees+"\n")

#------------------------------- FOR LIVE VIDEO -------------------------------#
cam = cv2.VideoCapture(0)

while(True):                                                                    # while loop for continuous analyzation of frames through video capture
    ret, frame = cam.read()
    h,w = frame.shape[:2]                                                       # gets the height and width of the frame for analyzation purposes
    imgXcenter = w/2
    imgYcenter = h/2
    det = Detector()                                                            # makes a new TargetDetector object
    proc = Processor()                                                          # makes a new TargetProcessor object
    if not ret:                                                                 # checks if boolean value ret is false
        continue

    threshold = det.threshold(minThreshold,maxThreshold,frame)                  # getting thresholded frame
    det.contours(threshold)                                                     # finding contours based on thresholded frame
    det.filterContours()                                                        # filtering the contours by size and number
    contours,index,corners = det.getContours()                                  # getting the contours, specific index, and array of corners


    if (corners is not None):                                                   # checking if the corners array returned is not null
        target = Target(corners)                                                # making a new Target object
        Imagewidth = target.getWidth()
        Xmid,Ymid = target.getCenter()
        cv2.line(frame,(Xmid,Ymid),(Xmid,Ymid),lightblue,5)
        cv2.drawContours(frame, contours, index, lightblue, 8)
        proc.calculate(focalLength,actualWidth,Imagewidth,Xmid-imgXcenter,imgYcenter-Ymid)
        displayValues()                                                         # method displays values in terminal

    cv2.imshow("drawContours", frame)                                           # shows the live feed frame by frame

    if cv2.waitKey(10) == 27:
        cv2.destroyAllWindows()
        break
