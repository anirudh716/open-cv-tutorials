import cv2 as cv

# img = cv.imread('Photos\photo1.jpg')
# cv.imshow('Scene', img)

# def rescaleFrame(frame, scale=0.75):
#     #works for images, videos, live videos
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width, height)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# resized_image = rescaleFrame(img, scale=.2)
# cv.imshow('Image', resized_image)

#reading videos
# capture = cv.VideoCapture('Videos/video1.mp4')
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     cv.imshow('Video', frame)
#     cv.imshow('Video_resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

def changeRes(capture, width, height):
    #works for live video(webcam)
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture(0)
changeRes(capture, 640, 480)
while True:
    isTrue, frame = capture.read()
    # cv.imshow('Video', frame)
    frame_resized = cv.resize(frame,(640,480))
    cv.imshow('Video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()