import os

print("os.name=", os.name)

os.chdir(r'C:\Data2\uploads')

print("os.getcwd()=", os.getcwd())

files = os.listdir(path=".")

print("files=", files)

for file in files:
    print(file)