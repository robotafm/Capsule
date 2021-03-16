import time
start_time = time.time()

from PIL import Image
import pytesseract
import cv2
import os

PAGE_COUNT_LIMIT = 10

image_path = 'D:/Data/testdata/img/'

image = image_path + 'Output.tiff'



# загрузить мультиизображение (многостраничное) из tiff и преобразовать его в opencv.mat
retval, mats = cv2.imreadmulti(image)

# сохраним картинку
filename = image_path + "test2.png"

index = 0
for mat in mats:
	index += 1
	if (index > PAGE_COUNT_LIMIT): 
		break
	filename = image_path + "testtiff" + str(index) + ".jpg"
	cv2.imwrite(filename, mat)



# показать выходные изображения mats[0], mats[1] ...
#cv2.imshow("Image", mats[0])

print("--- %s seconds ---" % (time.time() - start_time))
