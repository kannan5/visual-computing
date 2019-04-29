import numpy as np
import imutils
import cv2 as cv
from argparse import ArgumentParser


class TemplateMatching:
    def __init__(self, image='', template='', visualize_flag='', threshold=0):
        """
        Initialization function for Template Matching
        :param image: Source file location (PNG or JPG or other relevant image extensions allowed)
        :param template: Template file location (PNG or JPG or other relevant image extensions allowed)
        :param Visualize Flag: It will show the processing Image and Detected Area in Bounding Box
        :param Threshold: Threshold Value to be set.
        """
        self.image = image
        self.template = template
        self.visualize_flag = visualize_flag
        self.threshold = threshold

    def template_matching(self):
        """
        Parameters
    ----------
    image_path : string
        input image Path.
    template : string
        template file Path.
    visualize_flag : int, Either 0 or 1
        1 Enable the Visualize flag it will show the processing Image and Detected Area in Bounding Box
        0 Disable the Visualize flag
    threshold : int
        Setting the threshold value.
    Returns
    -------
    image : array, same shape as `image`
        Array in which indicates the `image`
        return the image with highlighted in bounding box
    match_found : bool, True or False
        True Indicates the match is found
        False Indicates there is no match found
        """
        image_file_path = self.image
        img = cv.imread(image_file_path)
        found = None
        match_found = None
        height, width = img.shape[:2]
        img_resize = cv.resize(img, (int(width/2), int(height/2)), interpolation=cv.INTER_CUBIC)
        img_gray = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
        template = cv.imread(self.template, 0)
        template = cv.Canny(template, 50, 200)
        cv.imshow("Image", template)
        cv.waitKey(0)
        (template_height, template_width) = template.shape[:2]
        for angle in np.arange(0, 300, 90):
            img_gray = imutils.rotate_bound(img_gray, angle)
            print(angle)
            cv.namedWindow("Image1", cv.WINDOW_NORMAL);
            cv.resizeWindow("Image1", 700, 700);
            cv.imshow("Image1", img_gray)
            cv.waitKey(0)
            if not match_found:
                print(match_found)
                for scale in np.linspace(0.2, 1.0, 20)[::-1]:
                    resize = imutils.resize(img_gray, width=int(img_gray.shape[1] * scale))
                    r = img_gray.shape[1] / float(resize.shape[1])
                    if resize.shape[0] < template_height or resize.shape[1] < template_width:
                        break
                    edged = cv.Canny(resize, 50, 200)
                    result = cv.matchTemplate(edged, template, cv.TM_CCOEFF_NORMED)
                    (_, maxVal, _, maxLoc) = cv.minMaxLoc(result)
                    if self.visualize_flag == 1:
                        clone = np.dstack([edged, edged, edged])
                        cv.rectangle(clone, (maxLoc[0], maxLoc[1]),
                                     (maxLoc[0] + template_width, maxLoc[1] + template_height),
                                     (0, 0, 255), 2)
                        cv.imshow("Visualize", clone)
                        cv.waitKey(0)
                    if found is None or maxVal > found[0]:
                        found = (maxVal, maxLoc, r)
                (_, maxLoc, r) = found
                (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
                (endX, endY) = (int((maxLoc[0] + template_width) * r), int((maxLoc[1] + template_height) * r))
                if maxVal > self.threshold:
                    # draw a bounding box
                    cv.rectangle(img, (startX, startY), (endX, endY), (0, 0, 255), 2)
                    match_found = True
                    cv.namedWindow("Image2", cv.WINDOW_NORMAL);
                    cv.resizeWindow("Image2", 1000, 700);
                    cv.imshow("Image2", img)
                    cv.waitKey(0)
        return match_found, img


if __name__ == "__main__":
    parse = ArgumentParser()
    parse.add_argument('-sf', '--source_img', help='Source File Path', type=str, required=True)
    parse.add_argument('-tf', '--template', help='Template File Path', type=str, required=True)
    parse.add_argument('-vf', '--flag', help='visualize Flag', type=int)
    parse.add_argument('-tv', '--threshold_value', help='Threshold Value', type=int)
    arguments = parse.parse_args()
    template_obj = TemplateMatching()
    template_obj.image = arguments.source_file
    template_obj.template = arguments.template
    template_obj.visualize_flag = arguments.flag
    template_obj.threshold = arguments.threshold
    result, img = template_obj.template_matching()

