import cv2


class TargetDetector:
    image = None
    contours = None
    mask = None

    """Defining all global variables"""
    def __init__(self):
        pass

    """Given the lower and upper HSV ranges, this takes out any unwanted 
parts of image"""
    def threshold(self, src, lower, upper):
        self.image = src
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        """Stores thresholded image in global variable"""
        self.mask = cv2.inRange(hsv, lower, upper)

    """Finds all contours given a thresholded image"""
    def findContours(self):
        _, self.contours, _ = cv2.findContours(self.mask, cv2.RETR_TREE, 
cv2.CHAIN_APPROX_SIMPLE)

    """Once contours have been found this removes any contours that are 
too small or do not resemble a shape"""
    def filterContours(self):

        for x in range(len(self.contours)):
            """Iterating through all contours to determine shape of that 
contour"""
            epsilon = 0.1 * cv2.arcLength(self.contours[x], True)
            approx = cv2.approxPolyDP(self.contours[x], epsilon, True)

            if cv2.contourArea(approx) > 500 and len(approx) >= 4:
                """using vertices of found shape, if there are more than 
four
                vertices and the area is greater than 500 pixels, the 
contour
                is good"""
                pass
            else:
                """if it does not pass these conditions then the contour 
is removed"""
                self.contours[x] = None

        """if all the contours are bad, then the entire contours array 
is set to None"""
        """However if even one set of contours is good, then the 
contours array is not sent to None"""
        for x in range (len(self.contours)):
            if not self.contours[x] is None:
                break
        self.contours = None

    """:returns the contours found"""
    def getContours(self):
        return self.contours

    """:returns the thresholded image"""
    def getMask(self):
        return self.mask
