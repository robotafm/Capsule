import os

print("os.name=", os.name)

os.chdir(r'C:\Data2\uploads')

print("os.getcwd()=", os.getcwd())

files = os.listdir(path=".")

print("files=", files)

for file in files:
    print(file)


path = r"D:\Data\testdata\djvu\Vas.djvu"

print("abspath=", os.path.abspath(path))
print("basename=", os.path.basename(path))
print("dirname=", os.path.dirname(path))
print("exists=", os.path.exists(path))
print("getsize=", os.path.getsize(path))
print("isfile=", os.path.isfile(path))
print("isdir=", os.path.isdir(path))
print("normcase=", os.path.normcase(path))
print("normpath=", os.path.normpath(path))