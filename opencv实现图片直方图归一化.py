import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
def hist_normalization(img,a = 0 , b = 255):
    c = img.min()   #最小值
    d = img.max()   #最大值
    out = img.copy()    #复制一个新的图像
    # 归一化
    out = (out - c) * (b - a) / (d - c) + a     # 归一化,照搬公式
    out[out<a] = a
    out[out>b] = b  # 将输出图像的值限制在[a,b]之间
    return out  # 返回归一化后的图像

# 读取图片
img = cv.imread('path')
H,W,C = img.shape # 获取图片的高、宽、通道数
out = hist_normalization(img)   # 图片归一化
plt.hist(out.ravel(),bins=255,rwidth = 0.8, range=(0,255))  # 绘制直方图
plt.savefig('output.png')   # 保存图片
plt.show()  # 显示图片

