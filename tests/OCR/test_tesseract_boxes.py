import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

filename = 'tmp/tests.png'

# read the image and get the dimensions
img = cv2.imread(filename)
h, w, _ = img.shape # assumes color image

# run tesseract, returning the bounding boxes
boxes = pytesseract.image_to_boxes(img) #use
print(pytesseract.image_to_string(img, lang='rus+eng')) #print identified text

# draw the bounding boxes on the image
for b in boxes.splitlines():
    b = b.split()
    cv2.rectangle(img, ((int(b[1]), h - int(b[2]))), ((int(b[3]), h - int(b[4]))), (0, 255, 0), 2)

# показать выходные изображения
cv2.imshow("Image", img)

#input('pause…')
