import cv2 as cv
import numpy as np


def morphological_operations():
    img = cv.imread(r'E:\pyworks\images.png')
    kernel = np.ones((5, 5), np.uint8)
    img_erosion = cv.erode(img, kernel=kernel, iterations=1)
    img_dilate = cv.dilate(img, kernel=kernel, iterations=1)
    cv.imshow('img_erosion', img_erosion)
    cv.imshow('img_dilate', img_dilate)
    cv.waitKey(0)
    cv.destroyAllWindows()


morphological_operations()