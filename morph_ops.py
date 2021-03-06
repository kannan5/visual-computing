import cv2 as cv
import numpy as np

def opening_n_closing():
    img = cv.imread(r'E:\pyworks\coin-detection.jpg')
    img = cv.resize(img, (700, 700))
    kernel = np.ones((3, 3), np.uint8)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    retval, threshold = cv.threshold(gray, 60, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    closing = cv.morphologyEx(threshold, cv.MORPH_CLOSE, kernel, iterations=3)
    dilate = cv.erode(closing, kernel, iterations=4)
    fg = cv.dilate(dilate, kernel, iterations=15)
    dist_trans = cv.distanceTransform(fg, cv.DIST_L2ś, 0)
    ret_val2, fg = cv.threshold(dist_trans, 0.05 * dist_trans.max(), 255, 0)
    cv.imshow('fg', fg)
    cv.imshow('dilate', dilate)
    cv.waitKey(0)
    cv.destroyAllWindows()


def detect():
    img = cv.imread(r'E:\pyworks\coin-detection.jpg')
    img = cv.resize(img, (700, 700))
    edges = cv.Canny(img, 100, 200)
    cv.imshow('win', edges)
    cv.waitKey(0)
    cv.destroyAllWindows()

#detect()
opening_n_closing()