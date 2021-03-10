import pytesseract
import cv2
import os

def get_text(file):
	"""
	Converting img file to text with tesseract library.
	"""
	# Путь к файлу-обработчику
	pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
	# загрузить образ
	image = cv2.imread(file)
	# преобразовать из cv2 BRG в понятный tesseract RGB
	img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	# преобразование картинки в текст и вывод на экран, обязательно указываем языки
	text = pytesseract.image_to_string(img_rgb, lang='rus+eng')
	return text

