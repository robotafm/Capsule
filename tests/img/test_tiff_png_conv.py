import time
start_time = time.time()

from PIL import Image
import pytesseract
import cv2
import os

image_path = 'D:/Data/testdata/img/'

image = image_path + 'test.tiff'

# загрузить мультиизображение (многостраничное) из tiff и преобразовать его в opencv.mat
retval, mats = cv2.imreadmulti(image)

# сохраним картинку
filename = image_path + "test2.png"
cv2.imwrite(filename, mats[0])

# показать выходные изображения mats[0], mats[1] ...
#cv2.imshow("Image", mats[0])

print("--- %s seconds ---" % (time.time() - start_time))
