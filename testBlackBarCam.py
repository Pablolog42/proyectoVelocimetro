import cv2
import pytesseract
from pytesseract import Output
 
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
 
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    xconfig = '--psm 9 --oem 3 -c tessedit_char_whitelist=0123456789.'
    
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    
    txt = pytesseract.image_to_string(blackAndWhiteImage, config=xconfig)
    
    print(txt)
    
    
    # Display the resulting frame
    cv2.imshow('frame', blackAndWhiteImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()