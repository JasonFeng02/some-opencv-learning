#用的opencv官方文档的图例
import cv2 as cv
import numpy as np
# 读取图片
img = cv.imread('path')
#读取图片高、宽、通道数
H,W,C = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])  # 原图像的三个点
pts2 = np.float32([[10,100],[200,50],[100,250]])  # 变换后的三个点
#其实也可以用rows,cols = img.shape[:2]获取高、宽，然后用np.float32([[0,0],[cols,0],[0,rows]])代替，就不用直接写坐标
#这个算不算仿射变换，官方文档就给了getaffineTransform函数
# 计算变换矩阵
M = cv.getAffineTransform(pts1,pts2)
# 变换
dst = cv.warpAffine(img,M,(W,H))
# 显示图片
cv.imshow('img',dst)
cv.waitKey(0)