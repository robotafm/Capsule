import time
start_time = time.time()

from PIL import Image
import pytesseract
import cv2
import os

image = r'D:\Data\testdata\imgOutput.tiff'

# загрузить мультиизображение (многостраничное) из tiff и преобразовать его в opencv.mats
retval, mats = cv2.imreadmulti(image)

# сохраним временную картинку, чтобы можно было применить к ней OCR
filename = "test1.png"
cv2.imwrite(filename, image)

# загрузка изображения в виде объекта image Pillow, применение OCR, а затем удаление временного файла
#text = pytesseract.image_to_string(Image.open(filename), lang='rus+eng')
#os.remove(filename)

#print(text)

# показать выходные изображения
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#input('pause…')

print("--- %s seconds ---" % (time.time() - start_time))
