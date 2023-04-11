import cv2 as cv
import numpy as np

img1 = cv.imread('src.jpg')
img2 = cv.imread('mask.png')

alpha = 0.1
  
dst = cv.addWeighted(img1, 1- alpha, img2, alpha, 0)
#dst2 = cv.addWeighted(img1, 0 , img2, 1- alpha, 0)

cv.imwrite('alpha_mask_.png', dst)
img3 = cv.imread('alpha_mask_.png')
  
#cv.imshow("alpha blending 1",img3)
cv.imshow('img',dst)
#cv.imshow('img2',dst2)

cv.waitKey(0)
  