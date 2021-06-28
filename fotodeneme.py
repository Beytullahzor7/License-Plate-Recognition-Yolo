import cv2
import numpy as np
import imutils
import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'

#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
img = cv2.imread('d.jpg')

img = imutils.resize(img, width= 500) #standart olarak genişliği 500 ayarladım

cv2.imshow("original", img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

gray = cv2.bilateralFilter(gray, 11, 17, 17)#Blur to reduce noise
cv2.waitKey(0)

edged = cv2.Canny(gray, 170, 200)
cv2.imshow("edged",edged)
cv2.waitKey(0)

cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#RETR LİST = tüm konturları gözden geçirir ancak herhangi bir bağlılık oluşturmaz oluşturmaz
#chain_approx_simple = tüm gereksiz noktaları kaldırır ve hafızadan tasarruf ederek konturu sıkıştırır

image1 = img.copy()
cv2.drawContours(image1, cnts, -1, (0,255,255), 3)
cv2.imshow("Canny after contouring", image1)
cv2.waitKey(0)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
NumberPlateCount = None

image2 = img.copy()
cv2.drawContours(image2 , cnts, -1, (0,255,0),3)
cv2.waitKey(0)

count = 0  #içerisinde plaka olma ihtimali en yüksek olan konturleri bulmak için for döngüsü oluşturduk
name = 1

for i in cnts:
    perimeter = cv2.arcLength(i, True) #konturun cevresini hesapladık, true değeri ile de kapalı şekil oldugunu belirttik
    approx = cv2.approxPolyDP(i, 0.02*perimeter, True) #cevrenin bir şekle yaklaşması için hassasiyet faktörü olan 0.02 ile carptık

    if(len(approx) == 4):    #if our approximated contour has four points, then we can assume that we have found our screen
        NumberPlateCount = approx

        x, y, w, h =cv2.boundingRect(i)                     #############################
        crp_img = img[y+3:y+h+3, x-1:x+w+1]                 #                           #
        cv2.imwrite(str(name)+ '.jpg', crp_img)             #                           # (y+h)
        name+=1                                             #                           #
        break                                               #############################
                                                          #(x,y)        (x+w)

cv2.drawContours(img, [NumberPlateCount], -1, (0,255,0), 3) #arac plakası olarak tanımladıgımız ana resim üzerine kontur uyguluyoruz
cv2.imshow("Final Image", img)
cv2.waitKey(0)

crop_img_loc = '1.jpg' #sadece plakayı alıyoruz
cv2.imshow("Cropped Image", cv2.imread(crop_img_loc))

text = pytesseract.image_to_string(crop_img_loc,config=tessdata_dir_config)
clean_text = re.sub('[\W_]+', ' ', text)
print("Arac Plakası: ", clean_text)

cv2.waitKey(0)
cv2.destroyAllWindows()















