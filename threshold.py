import numpy
import cv2 as cv


def threshold_img():
    img = cv.imread(r'E:\pyworks\source1.png')
    height, weight, channel = img.shape
    img = cv.resize(img, (1600, 1000))
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret_val, thresh_trunc_val = cv.threshold(img_gray, 240, 255, cv.THRESH_TRUNC)
    retval, simple_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
    gauss = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
    ret_otsu, otsu = cv.threshold(img_gray, 150, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C+cv.THRESH_OTSU)
    ret, otsu_binary_thresh = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    print("height,weight,channel", height, weight, channel)
    cv.imshow('simple thresholding', simple_binary)
    cv.imshow('Trunc thresholding', thresh_trunc_val)
    cv.imshow('gauss', gauss)
    cv.imshow('otsu', otsu)
    cv.imshow('otsu binary', otsu_binary_thresh)
    cv.waitKey(0)
    cv.destroyAllWindows()


threshold_img()
