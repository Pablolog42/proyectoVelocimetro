import cv2
import pytesseract
from functions import *

img = cv2.imread("testPantalla1-6.jpg")


gray = get_grayscale(img)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)

# Detect only digits
custom_config = r'--oem 3 --psm 6 outputbase digits'

text = pytesseract.image_to_string(img)
text1 = pytesseract.image_to_string(thresh)
text2 = pytesseract.image_to_string(opening)
text3 = pytesseract.image_to_string(canny)

total = [text1, text2,text3,text]

print(total)
