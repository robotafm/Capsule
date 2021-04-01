import time
start_time = time.time()

import cv2
import os

PAGE_COUNT_LIMIT = 3

image_path = 'D:/Data/testdata/img/'

image = image_path + 'Output.tiff'

# загрузить мультиизображение (многостраничное) из tiff и преобразовать его в opencv.mat
retval, mats = cv2.imreadmulti(image)
print("retval=", retval)
print("mats=", mats)

index = 0
for mat in mats:
	index += 1
	if (index > PAGE_COUNT_LIMIT): 
		break
	filename = image_path + "testtiff" + str(index) + ".png"
	cv2.imwrite(filename, mat)

# показать выходные изображения mats[0], mats[1] ...
#cv2.imshow("Image", mats[0])

print("--- %s seconds ---" % (time.time() - start_time))