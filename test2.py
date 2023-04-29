import cv2
import pytesseract
import os


# https://www.pythonfixing.com/2022/03/fixed-pytesseract-doesn-detect-number.html

xconfig = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'

# Picture List
plist = [x for x in os.listdir() if x.endswith(".jpg")]

for pt in plist:
    img = cv2.imread(pt)
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thr = cv2.threshold(src=gry, thresh=0, maxval=255, type=cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
    txt = pytesseract.image_to_string(thr)

    print(f"Imagen: {pt} -- Texto: {txt}")