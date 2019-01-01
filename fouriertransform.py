from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def fourier_trans(img):
    gray = Image.open(img).convert('L')
    dfft_array = (np.fft.fft2(gray))
    fourier_img = np.fft.fftshift(dfft_array)
    # fourier_img_1 = np.abs(np.log(fourier_img))
    img_size = fourier_img.shape
    fourier_img_clear = artifact_removal(fourier_img, img_size)
    fourier_img_1 = np.abs(np.log(fourier_img))
    plt.imshow(fourier_img_1, cmap='gray')
    plt.show()
    fourier_img = np.fft.ifftshift(fourier_img_clear)
    fourier_img = (np.fft.ifft2(fourier_img))
    # fourier_img = np.real(fourier_img)
    print(fourier_img)
    plt.imshow(np.abs(fourier_img), cmap='gray')
    plt.show()


def artifact_removal(img, img_shape):
    fourier_img = img.copy()
    x_end = img_shape[0]
    y_end = img_shape[1]
    x_centre = int(x_end / 2)
    y_centre = int(y_end / 2)
    val = 35

    for i in range(0, img_shape[0]):
        if not (x_centre - val) <= i <= (x_centre + val):
            fourier_img[i, y_centre] = 0
    for j in range(0, img_shape[1]):
            if not (y_centre - val) <= j <= (y_centre + val):
                fourier_img[x_centre, j] = 0
    print(fourier_img)
    return fourier_img


fourier_trans(r"E:\pyworks\Lecture1\latex_images_videos\smoke_lecture.png")
