import cv2 as cv
import numpy as np


def find_difference():
    img_gray = cv.imread(r"E:\pyworks\source1.png", cv.IMREAD_GRAYSCALE)
    sift = cv.xfeatures2d.SIFT_create()
    kp = sift.detect(img_gray, None)
    img_kp = cv.drawKeypoints(img_gray, kp, None)
    cv.imshow("Image",  img_kp)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    find_difference()
