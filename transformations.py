import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
img2 = cv.resize(img, (700,500))

#translation
def translate (img,x,y):
    transmat = np.float64([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img2, transmat, dimensions)

trans = translate(img2, 100, 100)


# -x --> left
# -y --> up
# x --> right
# y --> down

#rotation
def rotate(img2, angle, rotPoint = None):
    (height,width)= img2.shape[:2]

    if rotPoint is None:
        rotPoint= (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img2,rotMat,dimensions)

rotated = rotate(img2, 90)

#Resizing
resized = cv.resize(img2, (500,500), interpolation= cv.INTER_CUBIC)

#flipping
# 1 is for horizontal flip, 0 is for vertical flip, -1 is for both
flip=cv.flip(img2, 1)

#Cropping
cropped= img [200:400,300:400]

cv.imshow('img', cropped)
cv.waitKey(0)
