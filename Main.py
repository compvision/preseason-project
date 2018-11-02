import cv2
from TargetDetector import TargetDetector
from Target import Target
from TargetProcessor import TargetProcessor

class Main(object):
    """Runs everything"""
    def __init__(self, img):
        #init TargetDetector, Target, and TargetProcessor
        self.img = img
        self.detect = TargetDetector(self.img)
        self.detect.threshold()
        self.detect.contours()
        self.detect.filterContours()
        self.target = Target(self.img, self.detect.getContour())
        self.processor = TargetProcessor(self.img, self.target.xmin, self.target.xmax, self.target.ymin, self.target.ymax)
        self.processor.calculate()
    #show image with contours and the threshold image
    def display(self):
        cv2.imshow("image", self.detect.img)
        cv2.imshow("thresh", self.detect.thresh)

cam = cv2.VideoCapture(1)

cv2.namedWindow('Output',cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Output', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


while(True):
    ret, frame = cam.read()
    if not ret:
        continue

    main = Main(frame)
    print("Distance", main.processor.getDistance())
    print("Azimuth", main.processor.getAzimuth())
    print("Altitude", main.processor.getAltitude())
    main.display()

    if cv2.waitKey(10) == 27:
        cv2.destroyWindow('Output')
        break
