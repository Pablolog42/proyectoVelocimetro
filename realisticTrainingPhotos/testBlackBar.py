import cv2
import pytesseract
import os
import numpy as np

# https://www.pythonfixing.com/2022/03/fixed-pytesseract-doesn-detect-number.html
# Solo numeros
# OJO QUE ACA PSM8 o PSM 10 ARREGLA TODO AH
xconfig = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789.'

# Picture List
plist = [x for x in os.listdir() if (x.endswith(".jpg") or x.endswith(".png") or x.endswith(".jpeg"))]

for pt in plist:
    img = cv2.imread(pt)

    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Paso todo a ByN
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('Black white image', blackAndWhiteImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # alpha = 3.5  # Contrast control (1.0-3.0)
    # beta = 0  # Brightness control (0-100)
    # adjusted = cv2.convertScaleAbs(blackAndWhiteImage, alpha=alpha, beta=beta)

    # Se parsea la imagen byn
    txt = pytesseract.image_to_string(blackAndWhiteImage, config=xconfig)

    print(f"Imagen: {pt} -- Texto: {txt}")

    h, w, _ = img.shape  # assumes color image

    # run tesseract, returning the bounding boxes
    boxes = pytesseract.image_to_boxes(blackAndWhiteImage)  # also include any config options you use
    # draw the bounding boxes on the image
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    # show annotated image and wait for keypress
    #cv2.imshow(pt, img)
    #cv2.waitKey(0)
