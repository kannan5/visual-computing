from __future__ import print_function
import cv2 as cv
from skimage.feature import peak_local_max
from skimage.morphology import watershed
import numpy as np
import imutils
from scipy import ndimage


def img_watershed():
    img = cv.imread(r'E:\pyworks\watershed_coins_01.jpg')
    img = cv.resize(img, (700, 700))
    shifted = cv.pyrMeanShiftFiltering(img, 21, 51)
    gray = cv.cvtColor(shifted, cv.COLOR_BGR2GRAY)
    thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    EDT = ndimage.distance_transform_edt(thresh)
    local_max = peak_local_max(EDT, indices=False, min_distance=30, labels=thresh)
    markers = ndimage.label(local_max, structure=np.ones((3,3)))[0]
    labels = watershed(-EDT, markers, mask=thresh)
    for label in np.unique(labels):
        if label == 0:
            continue
        mask = np.zeros(gray.shape, dtype = "uint8")
        mask[labels == label] = 255
        cntrs = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cntrs)
        c = max(cnts, key=cv.contourArea)
        ((x, y), r) = cv.minEnclosingCircle(c)
        cv.circle(img, (int(x), int(y)), int(r), (0, 255, 0), 2)
        cv.putText(img, "#{}".format(label), (int(x)-10, int(y)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255, 2))
    cv.imshow("win1", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


img_watershed()
