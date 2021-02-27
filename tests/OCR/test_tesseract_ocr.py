import time
start_time = time.time()

from PIL import Image
import pytesseract
import cv2
import os

image_path = r'C:\Data2\OCR\text.png'

preprocess = "none"

# Путь к файлу-обработчику
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# загрузить образ
image = cv2.imread(image_path)

# сохраним временную картинку
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, image)

# загрузка изображения в виде объекта image Pillow, применение OCR, а затем удаление временного файла
text = pytesseract.image_to_string(Image.open(filename), lang='rus+eng')
os.remove(filename)

print(text)

# показать входные изображения
cv2.imshow("Image", image)

print("--- %s seconds ---" % (time.time() - start_time))
