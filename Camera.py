import numpy as np
import cv2
import math
import os

from Main import Main

cam = cv2.VideoCapture(1)

cv2.namedWindow('Output',cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Output', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while(True):
    ret, frame = cam.read()
    if not ret:
        continue

    main = Main(frame)
    print("Distance", main.distance())
    print("Azimuth", main.azimuth())
    print("Altitude", main.altitude())
    main.display()

    if cv2.waitKey(10) == 27:
        cv2.destroyWindow('Output')
        break
