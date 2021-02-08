import time
start_time = time.time()

import os

os.system('C:\Windows\System32\notepad.exe')

#os.system('" C:\Program Files (x86)\DjVuLibre\ddjvu.exe"'
#          + ' -format=tiff '
#          + ' " D:\Capsule\tests\djvu\test_files\Vas.djvu"'
#          + ' " D:\Capsule\tests\djvu\test_files\Output.tiff"')

print("--- %s seconds ---" % (time.time() - start_time))
