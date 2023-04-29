
import cv2
import pytesseract
import os


# https://www.pythonfixing.com/2022/03/fixed-pytesseract-doesn-detect-number.html

xconfig = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'

# Picture List
plist = [x for x in os.listdir() if x.endswith(".jpeg")]

for pt in plist:
    img = cv2.imread(pt)
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thr = cv2.threshold(src=gry, thresh=0, maxval=255, type=cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
    txt = pytesseract.image_to_string(thr)

    print(f"Imagen: {pt} -- Texto: {txt}")

    h, w, _ = img.shape # assumes color image

    # run tesseract, returning the bounding boxes
    boxes = pytesseract.image_to_boxes(img) # also include any config options you use


    # draw the bounding boxes on the image
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    # show annotated image and wait for keypress
    #cv2.imshow(pt, img)
    #cv2.waitKey(0)