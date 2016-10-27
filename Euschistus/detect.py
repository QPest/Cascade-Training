import cv2
import numpy as np
import os

cascade = cv2.CascadeClassifier('data/cascade.xml')

for file_type in ['Euschistus Heros']:
    count = 1
    for image in os.listdir(file_type):
        try:
            current_image_path = str(file_type) + '/' + str(image)
            img = cv2.imread(current_image_path)
            img = cv2.resize(img, (300, 300))

            euschistus = cascade.detectMultiScale(img)

            for (x, y, w, h) in euschistus:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow('img' + str(count), img)

            count += 1
        except Exception as e:
            print(str(e))

k = cv2.waitKey(0)

cv2.destroyAllWindows()
