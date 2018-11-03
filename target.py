import cv2


class Target:

    width = 0
    height = 0
    centerX = 0
    centerY = 0
    xMin = 0
    xMax = 0
    yMin = 0
    yMax = 0
    contours = None

    """Defining all global variables"""
    """Target requires a set of contours to be created"""
    def __init__(self, cont):
        self.contours = cont

    """Simple functions to find the least and greatest amounts in an 
array"""
    """Iterates through every point in an array to find 
greatest/least"""
    def findLeast(self, a):
        least = 10000
        for i in range(len(a)):
            if a[i] < least:
                least = a[i]
        return least

    def findGreatest(self, a):
        greatest = -1
        for i in range(len(a)):
            if a[i] > greatest:
                greatest = a[i]
        return greatest

    def getHeight(self):
        for x in range(len(self.contours)):
            """If the current contour is bad, it's removed through 
filtering in targetDetector"""
            """This only runs if the contour is good"""
            if self.contours[x] is not None:
                epsilon = 0.1 * cv2.arcLength(self.contours[x], True)
                approx = cv2.approxPolyDP(self.contours[x], epsilon, 
True)
                """Getting the vertices of our detected shape"""

                """Gathers all the y points in the vertices of the shape 
and determines 
                the greatest and the least"""
                yPoints = []
                for a in range(len(approx)):
                    for b in range(len(approx[a])):
                        yPoints.append(approx[a][b][1])

                self.yMin = self.findLeast(yPoints)
                self.yMax = self.findGreatest(yPoints)

                """Once the greatest and least y point have been found, 
it is easy to find height"""
                self.height = self.yMax - self.yMin

                return self.height

    def getWidth(self):
        for x in range(len(self.contours)):
            """If the current contour is bad, it's removed through 
filtering in targetDetector"""
            """This only runs if the contour is good"""
            if self.contours[x] is not None:
                epsilon = 0.1 * cv2.arcLength(self.contours[x], True)
                approx = cv2.approxPolyDP(self.contours[x], epsilon, 
True)
                """Getting the vertices of our detected shape"""

                """Gathers all the x points in the vertices of the shape 
and determines 
                the greatest and the least"""
                xPoints = []
                for a in range(len(approx)):
                        for b in range(len(approx[a])):
                           xPoints.append(approx[a][b][0])

                self.xMin = self.findLeast(xPoints)
                self.xMax = self.findGreatest(xPoints)

                """Once the greatest and least x point have been found, 
it is easy to find width"""
                width = self.xMax - self.xMin

                return width

    """Given the max and min x and y coordinates, this determines the 
center of the target"""
    def getCenter(self):
        self.centerX = (self.xMax + self.xMin) / 2
        self.centerY = (self.yMax + self.yMin) / 2

        return self.centerX, self.centerY
