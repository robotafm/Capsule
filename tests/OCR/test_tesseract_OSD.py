import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

filename = r'D:\Data\testdata\img\OCR\test_rotate.png'

# read the image
img = cv2.imread(filename)

# For testing:
# # Prepare image to OCR
# image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# image_bin = cv2.adaptiveThreshold(image_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY ,41,3)
# cv2.imshow("Original", img)
# cv2.imshow("Gray", image_gray)
# cv2.imshow("Bin", image_bin)

# run tesseract, returning binary text ALTO xml
OSD = pytesseract.image_to_osd(img) #use

print(OSD)

#input('pause…')
