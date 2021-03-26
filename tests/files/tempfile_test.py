import tempfile
import os

with tempfile.NamedTemporaryFile() as fp:
    print(fp.name)  # путь к файлу
    fp.write(b'Hello world!')
    fp.seek(0)
    print(fp.read())

# Указание метод открытия, по умолчанию "w+b"
tempfile.NamedTemporaryFile(mode='w') 

# В отличии от NamedTemporaryFile не имеет имени и 
# может быть не виден файловой системе 
tempfile.TemporaryFile()

# Временная директория, после закрития удаляется со всеми файлами
with tempfile.TemporaryDirectory() as temp:
    with open(os.path.join(temp, '1.txt'), 'w') as f:
        f.write('hello')

# Если надо вручную очистить (можно только 1 раз, после она будет удалена):
tmp = tempfile.TemporaryDirectory()
with open(os.path.join(tmp.name, '1.txt'), 'w') as f:
    f.write('hello')
tmp.cleanup()  # очистка

# Узнать где хранятся временные файлы:
tempfile.gettempdir()

# Прямое указание места создания временного файла/директории.
tempfile.NamedTemporaryFile(dir='D:/Data')