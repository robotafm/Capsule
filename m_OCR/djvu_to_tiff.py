import os

# Обрати внимание на "Program Files (x86)" и C:\ без кавычек. 
# Только так это работает в Windows!
Ddjvu_cmd = r'C:\"Program Files (x86)"\DjVuLibre\ddjvu.exe -format=tiff'

input_file = r'D:\Data\testdata\djvu\Vas.djvu'

output_file = r'D:\Data\testdata\djvu\Output.tiff'

def djvu_to_tiff(input_file=input_file, output_file=output_file):
    """
    Function for convertion .djvu files to .tiff (multipage)
    """

    # Пример генерации строки команды из нескольких строк:
    comm = Ddjvu_cmd + " " + input_file + " " + output_file

    # Test code:
    #print(comm)

    #Пробуем запустить конвертацию из Djvu в Tiff
    os.system(comm)

def main():
    djvu_to_tiff()

if __name__ == '__main__':
    main()
