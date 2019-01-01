import cv2   as cv
import  numpy as np

def inpainting():
    path = r'E:\pyworks\\'
    img = path +'pexels-photo.jpg'
    img = cv.imread(img)
    #img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    height_org, weight_org,depth = img.shape
    print(height_org, weight_org)
    mask_creation(img,height_org,weight_org)

def mask_creation(img,height_org,weight_org):
    #roi = cv.selectROI(img)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask = cv.inRange(img, lower_red, upper_red)
    limit = 200
    mask = np.zeros(img.shape,dtype='uint8')
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            pixel = img.item(i, j, 2)
            for k in range (0, img.shape[2]):
                if pixel > limit:
                   mask[i, j, k] = 255
    cv.imshow('img1', mask)
    mask = cv.cvtColor(mask,cv.COLOR_BGR2GRAY)
    dst = cv.inpaint(img, mask, 3, cv.INPAINT_TELEA)
    cv.imshow('img', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

inpainting()