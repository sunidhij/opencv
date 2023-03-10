import cv2 as cv

img =cv.imread('cat.jpg')
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

resized_image = rescaleFrame(img, scale = 0.2)
#cv.imshow('Img', resized_image )

#converting to grayscale
#gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
#cv.imshow('GRAY', gray)

#blurring
#blur = cv.GaussianBlur(resized_image, (7,7),cv.BORDER_DEFAULT) 
#cv.imshow('blur',blur)

#edge cascade
# canny = cv.Canny(resized_image,80,100)
# cv.imshow('blur',canny)

# #dilating the image
# dilated = cv.dilate(canny,(7,7), iterations=3)
# cv.imshow('dil',dilated)

# #eroding
# eroded= cv.erode(dilated, (3,3), iterations=3)
# cv.imshow('erod', eroded) 

#resisze
resized = cv.resize(img,(400,400), interpolation=cv.INTER_CUBIC)
cv.imshow('res', resized)

#crop
cropped= resized[50:200,200:400]
cv.imshow('crop', cropped)
cv.waitKey(0)
