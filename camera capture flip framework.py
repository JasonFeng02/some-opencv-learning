import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret,frame = cap.read()
    if not ret:
        print("Cannot receive frame (stream)")
        break
    r,h,c,w = 250,90,400,125
    track_window = (c,r,w,h)
    roi = frame[r:r+h,c:c+w]
    hsv_roi = cv.cvtColor(roi,cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv_roi,np.array((0.,60.,32.)),np.array((180.,255.,255.)))
    roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
    cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
    term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,10,1)
    while True:
        ret,frame = cap.read()
        if not ret:
            print("Cannot receive frame (stream)")
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        ret,track_window = cv.CamShift(dst,track_window,term_crit)
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv.polylines(frame,[pts],True, 255,2)
        cv.imshow('img2',img2)
        k = cv.waitKey(60) & 0xff
        if k == 27:
            break
cap.release()
cv.destroyAllWindows()

