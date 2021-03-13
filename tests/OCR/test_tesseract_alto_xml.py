import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

filename = r'C:\Data2\OCR\text.png'
output_file = r'C:\Data2\OCR\alto.xml'

# read the image
img = cv2.imread(filename)

# run tesseract, returning binary text ALTO xml
alto_xml = pytesseract.image_to_alto_xml(img, lang='rus+eng') #use

# save output xml
f = open(output_file, "wb")
f.write(alto_xml)
f.close()

#input('pause…')
