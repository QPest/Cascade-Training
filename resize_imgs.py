import cv2
import numpy as np
import os


def resize_images():
    pic_num = 1
    print "called"
    if not os.path.exists('positive'):
        os.makedirs('positive')
    for file_type in ['CroppedImages']:
        for img in os.listdir(file_type):
            try:
                current_image_path = str(file_type)+'/'+str(img)
                print current_image_path
                img = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(img, (50, 50))
                #cv2.imshow("Image", resized_image)
                #cv2.waitKey(0)
                cv2.imwrite("posIn/" + str(pic_num) + ".jpg", resized_image)
                pic_num += 1
            except Exception as e:
                print(str(e))

def create_info():
    listAll = open('info.lst', 'w')
    if not os.path.exists('info'):
        os.makedirs('info')
    for file_type in ['info']:
        for file in os.listdir(file_type):
            try:
                listAll.write("%s\n" % file)
            except Exception as e:
                print(str(e))
    listAll.close()

resize_images()
