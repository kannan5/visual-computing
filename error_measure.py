import numpy as np
import cv2 as cv
from sklearn.metrics import mean_squared_error
from skimage.measure import compare_ssim
import imutils


def mse_error(image1, image2):
    error = np.sum((image1.astype("float") - image2.astype("float"))**2)
    error /= float(image1.shape[0] * image1.shape[1])
    return error


def image_bright(img):
    alpha = 2
    beta = 50
    result = cv.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)
    cv.imwrite(r'E:\pyworks\result.png', result)


def find_error():
        image1 = cv.imread(r'E:\pyworks\jp_gates_original.png')
        image1 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
        image2 = cv.imread(r'E:\pyworks\jp_gates_photoshopped.png')
        image2 = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)
        image3 = imutils.rotate(image2, angle=180)
        m = mean_squared_error(np.array(image1), np.array(image2))
        n = compare_ssim(np.array(image1), np.array(image2))
        print("mean square:", m)
        print("ssim: ", n)


find_error()
