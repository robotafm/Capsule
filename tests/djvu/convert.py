import time
start_time = time.time()

import os

#Пример запуска программы из Python:
#os.system('"C:/Windows/System32/notepad.exe"')

#Пример генерации строки команды из нескольких строк:
comm = r'C:\"Program Files (x86)"\DjVuLibre\ddjvu.exe -format=tiff "D:\Capsule\tests\djvu\test_files\Vas.djvu" "D:\Capsule\tests\djvu\test_files\Output.tiff"'
#Обрати внимание на "Program Files (x86)" и C:\ без кавычек. Только так это работает в Windows!
print (comm)

#Пробуем запустить конвертацию из Djvu в Tiff
os.system(comm)

print("--- %s seconds ---" % (time.time() - start_time))
