import cv2 as cv
import numpy as np
path = 'C:\\Users\JasonFeng\Desktop\pic.jpg'
img = cv.imread(path)
orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(img, None)
img2 = cv.drawKeypoints(img, kp1, None, color=(0, 255, 0), flags=0)
cv.imshow('img2', img2)
cv.waitKey(0)