import cv2
import numpy as np
import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
#tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'

net = cv2.dnn.readNet('yolov3_training_last.weights', 'yolov3_testing.cfg')
classes = []
with open("classes.txt", "r") as f:
    classes = f.read().splitlines()

cap = cv2.VideoCapture('video.mp4')

font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(100, 3))
count = 0

while True:
    _, img = cap.read()
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1/255, (416,416), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []


    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id] #nesnenin tanımlandıgından emin olmak için güven seviyesi yüksek olan classları aldık
            if confidence > 0.2:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label + " " + confidence, (x, y - 5), font, 2, (255, 255, 255), 2)

            imgRoi = img[y+3:y+h+3, x:x+w+1] #arac plakasını video içerisinden resim olarak aldım

            try:
                cv2.imshow("ROI", imgRoi)
            except:

                continue

            try:
                text = pytesseract.image_to_string(imgRoi, config='--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata" --psm 9 --oem 3')
                clean_text = re.sub('[\W_]+', '', text)
                liste = clean_text.split()
                for i in liste:
                    result = re.findall("[^A-Za-z-][0-9]+[A-Z]+[0-9]+",i)
                    if result:
                        print("Arac Plakası: ", result)

                #if len(clean_text) >= 7:

                    #print("Arac Plakası: ", clean_text)

            except:
                continue

    #print(imgRoi.shape)

    cv2.imshow('Image', img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/NoPlate_"+str(count) +".jpg", imgRoi)
        #cv2.imwrite("NoPlate_"+str(count) +".jpg", imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)

        text = pytesseract.image_to_string(imgRoi, config='--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata" --psm 9 --oem 3')
        clean_text = re.sub('[\W_]+', ' ', text)
        liste = clean_text.split()
        for i in liste:
            result = re.findall("[^A-Za-z-][0-9]+[A-Z]+[0-9]+", i)
            if result:
                print("Arac Plakası: ", result)

        cv2.imshow("Image", img)
        cv2.waitKey(500)
        count += 1


cap.release()
cv2.destroyAllWindows()

