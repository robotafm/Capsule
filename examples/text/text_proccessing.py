#Предварительная обработка "сырого" текста, полученного из OCR

import string

text = "TExt"

#Открываем файл
f = open(r'D:\Data\testdata\text\News.txt', 'rb')

#Считываем текст
text = f.read()

#Закрываем файл
f.close()

print("text=", text)
print("text.decode('utf-8')=", text.decode('utf-8'))

text = text.decode('utf-8')

#Переводим текст в нижний регистр
text = text.lower()

print (text)

#Набор символов пунктуации
print(string.punctuation)

#Набор символов пунктуации и спецсимволов
spec_chars = string.punctuation + '\n\xa0«»\t—…'

#Удаляем все спецсимволы и символы пунктуации
text = "".join([ch for ch in text if ch not in spec_chars])

print (text)

print('%d %s, %d %s' % (6, 'bananas', 10, 'lemons'))

