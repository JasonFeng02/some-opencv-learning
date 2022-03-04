import cv2 as cv
import numpy as np
image = input('path:')
img = cv.imread(image)
#读取图片后进行灰度化
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 二值化，阈值100,大于100的设置为255，小于100的设置为0,可选在这一步之前对图片进行高斯模糊，降噪
ret, binary = cv.threshold(gray, 100, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
# 膨胀
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
dst = cv.dilate(dst, kernel)
# 腐蚀
dst = cv.erode(dst, kernel)
#看情况决定是否需要再次膨胀，这里直接imshow，没写result那些，可以写cv.putText对结果图片进行标注
cv.imshow('binary', dst)
cv.waitKey(0)
