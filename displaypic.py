import cv2 as cv

img = cv.imread('Photos/dog.jpeg')

cv.imshow('Dog', img)

cv.waitKey(0)
