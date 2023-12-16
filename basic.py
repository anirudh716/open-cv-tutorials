import cv2 as cv
img = cv.imread('Photos/photo3.jpg')
# cv.imshow('image', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

#blur
blurred = cv.GaussianBlur(img,(13,13),cv.BORDER_DEFAULT)
# cv.imshow('blur', blurred)

#edge cascade
canny = cv.Canny(img, 125,175)
# cv.imshow('cnny', canny)

#dilating the images
dilated = cv.dilate(canny, (3,3), iterations=3)
# cv.imshow('dilated', dilated)

eroded = cv.erode(dilated, (3,3), iterations=3)
# cv.imshow('erode', eroded)

imag = cv.imread('Photos/photo1.jpg')
# cv.imshow('image', imag)

#resize
resized = cv.resize(imag, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#cropping
croped = imag[50:200, 50:400]
cv.imshow("crop", croped)
cv.waitKey()