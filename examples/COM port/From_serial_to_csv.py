from tkinter import *
import serial
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter
import csv
import time

# Constants:
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']
folder_to_save_file = "D:/Data/csv/"

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def readrow(port):
    """ Read one int value from COM port

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    out = ""
    data = 0
    # Check if the message is already finished
    while not out.endswith('[3;05f'):
        # Save the last received characters
        # A `bytes` object is encoded in 'ISO-8859-1'
        received_chars = str(port.read(), 'ISO-8859-1')

        # Clear data
        if received_chars == 'þ':
            received_chars = ''
        if received_chars == '':
            received_chars = '\n'

        # Add them to `out`
        out += received_chars
                    
        # Find data index
        index = out.rfind('[3;05f')
        if index != -1:
            result = out[index-4:index]
            data = int(result)
    return(data)

# Open COM port
ser = serial.Serial(port=serial_ports()[1], baudrate=115200, bytesize=8, 
                    parity='N', stopbits=1, timeout=0.1, 
                    xonxoff=0, rtscts=0)

# Create filename to save data
current_time = time.localtime()
file_name = (folder_to_save_file+str(current_time.tm_hour)+"_"+str(current_time.tm_min)+" "+
            str(current_time.tm_mday)+"."+str(current_time.tm_mon)+"."+str(current_time.tm_year)+".csv")
print(file_name)
counter = 0
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL) 
    while counter<1000:
        data = readrow(ser)
        writer.writerow([data, "info"])
        counter = counter + 1

# Close COM port
ser.close()