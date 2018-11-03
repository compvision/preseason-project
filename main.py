import numpy as np
import cv2
import target
import targetDetector
import targetProcessor

"""Defining focal length and the actual width of our target (actual 
width may not
be entirely correct)"""
FOCAL_LENGTH = 538
ACTUAL_WIDTH = 17.5

"""Creating new target processors and detectors"""
myProcessor = targetProcessor.TargetProcessor()
myDetector = targetDetector.TargetDetector()

"""Change video capture port to 1 when testing with camera"""
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, src = cap.read()

    """only stop program when escape is pressed or no video frame is 
recieved"""
    if cv2.waitKey(1) == 27 or not ret:
        break

    """Defining lower and upper threshold values which determine 
detected objects"""
    lower = np.array([70, 33, 173])
    upper = np.array([195, 113, 215])

    """Threshold using lower and upper colors (above)"""
    myDetector.threshold(src, lower, upper)
    myDetector.findContours()
    myDetector.filterContours()
    """Once contours have been found and filtered they can be used"""
    contours = myDetector.getContours()
    mask = myDetector.getMask()
    """Get the thresholded image so it can be displayed"""

    """This only runs if contours were found"""
    if contours is not None:

        """Creating a new object with the contours we found"""
        thisTarget = target.Target(contours)
        """and finding the height and width"""
        height = thisTarget.getHeight()
        width = thisTarget.getWidth()
        """as well as the center of the target."""
        centerX, centerY = thisTarget.getCenter()

        """Once height, width, and center have been found, we can 
calculate the distance
        azimuth, and altitude of our camera relative to the target."""
        myProcessor.calculate(FOCAL_LENGTH, ACTUAL_WIDTH, width, src, 
centerX, centerY)
        distance = myProcessor.getDistance()
        azimuth = myProcessor.getAzimuth()
        altitude = myProcessor.getAltitude()

        """Printing out all our found info"""
        print("Width of Rect: " + str(width) + " pixels")
        print("Height of Rect: " + str(height) + " pixels")
        print("Center of Rectangle: (" + str(centerX) + ", " + 
str(centerY) + ")")
        print("")
        print("Distance of Rect: " + str(distance) + " centimeters")
        print("Azimuth: " + str(azimuth) + " degrees")
        print("Altitude: " + str(altitude) + " degrees")

        """Drawing contours on our image for testing purposes"""
        cv2.drawContours(src, contours, -1, (0, 255, 0), 3)
        cv2.line(src, (centerX, centerY), (centerX, centerY), (0, 255, 
0), 5)
        break

    """Displaying our image with contours drawn on and displayed 
thresholded image"""
    cv2.imshow("Capture", src)
    cv2.imshow("Thresholded", mask)


"""When everything done, release the capture"""
cap.release()
cv2.destroyAllWindows()
