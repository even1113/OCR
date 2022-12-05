# 导入相关的库
from PIL import Image
import cv2 as cv
import numpy as np
import torch
import pytesseract
import easyocr
import cv2
import os
import re
import pandas as pd
import openpyxl


# binary
def threshold_custome(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]  # 去shape中的前两个通道
    m = np.reshape(gray, [1, w * h])  # reshape()函数重新定义了原张量的阶数,弄成了1行w*h列的一个向量了。
    mean = m.sum() / (w * h)  # 求出整个灰度图像的平均值
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    return binary


bilinear = cv.imread('./test/bilinear.png')

bilinear_gray = cv.imread('./test/bilinear.png', 0)
cv.imwrite('bilinear_gray.png', bilinear_gray)

bilinear_thre = threshold_custome(bilinear)
cv.imwrite('bilinear_thre.png', bilinear_thre)


