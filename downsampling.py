import matplotlib.pyplot as mplt
from PIL import Image
import numpy as np
from sklearn.metrics import mean_squared_error


def down_sample(img):
    image_size = np.shape(img)
    size_x = int(image_size[0] / 2)
    size_y = int(image_size[1] / 2)
    img = img.resize((size_x, size_y), Image.ANTIALIAS)
    return img


def up_sample(img):
    image_size = np.shape(img)
    size_x = round(image_size[0] * 2) + 1
    size_y = round(image_size[1] * 2) + 1
    img = img.resize((size_x, size_y), Image.ANTIALIAS)
    return img


def compare_png_jpg(png_img, jpg_img):
    c_img_mean = mean_squared_error(np.array(png_img), np.array(jpg_img))
    c_img_diff = (np.subtract(np.array(png_img), np.array(jpg_img)))
    return c_img_mean, c_img_diff


if __name__ == '__main__':
    img = Image.open(r'E:\pyworks\Lecture2\Assignment_data\mandarin_monkey.PNG').convert('L')
    img_ds = down_sample(img)
    img_up = up_sample(img_ds)
    # mse = ((np.array(img) - np.array(img_up)) ** 2).mean(axis=0)
    img_mean = mean_squared_error(np.array(img), np.array(img_up))
    img_diff = (np.subtract(np.array(img),  np.array(img_up)))
    mplt.imshow(img_ds, cmap='gray')
    mplt.show()
    print(img_mean)
    print(img_diff)
    img_png = Image.open(r'E:\pyworks\Lecture2\Assignment_data\mandarin_monkey.PNG').convert('L')
    img_jpg = Image.open(r'E:\pyworks\Lecture2\Assignment_data\mandarin_monkey.jpg').convert('L')
    cmp_img_mean, cmp_img_diff = compare_png_jpg(img_png, img_jpg)
    print(cmp_img_mean)
    print(cmp_img_diff)
