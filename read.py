import cv2 as cv

# img = cv.imread('Photos\photo1.jpg')
# cv.imshow('Scene', img)

#reading videos
capture = cv.VideoCapture('Videos/video1.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# cv.waitKey(0)