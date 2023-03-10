import cv2 as cv

img =cv.imread('cat.jpg')
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

resized_image = rescaleFrame(img, scale = 0.2)
cv.imshow('Img', resized_image )

#converting to grayscale
#gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
#cv.imshow('GRAY', gray)

#blurring
blur = cv.GaussianBlur(resized_image, (7,7),cv.BORDER_DEFAULT) 
cv.imshow('blur',blur)

cv.waitKey(0)