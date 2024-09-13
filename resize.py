import cv2 as cv

img = cv.imread(Photos/dog.jpeg)

cv.imshow('Dog', img)

cv.waitKey(0)


# resize function
#image, video and live video
def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width, heigth)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resolution function
#only live videos

