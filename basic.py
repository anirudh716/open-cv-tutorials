import cv2 as cv
img = cv.imread('Photos/photo3.jpg')
cv.imshow('image', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
cv.waitKey()