import subprocess as sp
import os
import stat


input_file = r'D:\Data\testdata\djvu\test2_multipage.djvu'
output_file = r'D:\Data\testdata\djvu\page%d.tiff' # %d -> page number (if -eachpage)

dirpath = r'C:\Program Files (x86)\DjVuLibre'
filename = r'ddjvu.exe'

#os.chmod(dirpath, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777

cmd_args = []
cmd_args.append(os.path.join(dirpath,filename))
cmd_args.append('-format=tiff')
cmd_args.append('-eachpage')
cmd_args.append('-skip')
cmd_args.append(input_file)
cmd_args.append(output_file)
print(cmd_args)
child = sp.Popen(cmd_args)

# print(subprocess.call(comm))