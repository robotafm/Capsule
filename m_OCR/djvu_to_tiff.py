import os
import time

# Обрати внимание на "Program Files (x86)" и C:\ без кавычек. 
# Только так это работает в Windows!
Ddjvu_cmd = r'C:\"Program Files (x86)"\DjVuLibre\ddjvu.exe -format=tiff -eachpage -skip'
input_file = r'D:\Data\testdata\djvu\Mark.djvu'
output_file = r'D:\Data\testdata\djvu\page%d.tiff' # %d -> page number (if -eachpage)

def djvu_to_tiff(input_file=input_file, output_file=output_file):
    """
    Function for convertion .djvu files to .tiff (each page in a separate file)
    """
    # Ddjvu result command:
    comm = Ddjvu_cmd + " " + input_file + " " + output_file
    # Run
    os.system(comm)

def main():
    # For testing runtime. 
    start_time = time.time()
    djvu_to_tiff()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
