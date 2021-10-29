import time
# запуск таймера для определения общего времени работы скрипта
start_time = time.time()

import pytesseract
import cv2
import os

image_path = r'C:\Data2\OCR\text.png'

# Путь к файлу-обработчику
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# загрузить образ
image = cv2.imread(image_path)

# преобразовать из cv2 BRG в понятный tesseract RGB
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# преобразование картинки в текст и вывод на экран, обязательно указываем языки
text = pytesseract.image_to_string(img_rgb, lang='rus+eng')

print (text)

# показать входное изображения
cv2.imshow("Image", image)

# показать, сколько времени заняла обработка
print("--- %s seconds ---" % (time.time() - start_time))
