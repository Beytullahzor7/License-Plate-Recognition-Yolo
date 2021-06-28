import cv2
import  pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'

img = cv2.imread('ornek3.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#### Detecting Characters  ######
hImg,wImg,_ = img.shape
cong = r'--oem 3 --psm 6 outbase digits'
boxes = pytesseract.image_to_data(img, config= tessdata_dir_config)
print(boxes)

for x,b in enumerate(boxes.splitlines()):

    if x!=0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 2)
            cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

cv2.imshow('result', img)
cv2.waitKey(0)
