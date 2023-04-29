# Picture List
import numpy as np
import cv2
import os

import pytesseract

plist = [x for x in os.listdir() if (x.endswith(".jpg") or x.endswith(".png"))]

for pt in plist:
    img = cv2.imread(pt)

    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    img = cv2.GaussianBlur(img, (1, 1), 0)
    cv2.imshow(img)
    cv2.waitKey(0)

    text = pytesseract.image_to_string(pt,img)
    print(text)
