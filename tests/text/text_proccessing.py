#Предварительная обработка "сырого" текста, полученного из OCR

import string

#Открываем файл
f = open('tmp/text.txt', 'r')

#Считываем текст
text = f.read()

#Закрываем файл
f.close()

#Переводим текст в нижний регистр
text = text.lower()

print (text)

#Набор символов пунктуации
print(string.punctuation)

#Набор символов пунктуации и спецсимволов
spec_chars = string.punctuation + '\n\xa0«»\t—…'

#Добавить замену дефиса в конце строки пустой строкой

#Удаляем все спецсимволы и символы пунктуации
text = "".join([ch for ch in text if ch not in spec_chars])

print (text)


