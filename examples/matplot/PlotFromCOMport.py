from tkinter import *
import serial
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter

# Constants:
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']

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


# Mathplotlib:


def init():
    line.set_ydata([np.nan] * len(x))
    return line,

def animate(i):
    # Add next value
    data.append(np.random.randint(0, max_rand))
    line.set_ydata(data)
    # plt.savefig('e:\\python temp\\fig_{:02}'.format(i))
    print(i)
    return line,

max_x = 100
max_rand = 100

data = deque(np.zeros(max_x), maxlen=max_x)  # hold the last values
x = np.arange(0, max_x)

fig, ax = plt.subplots()
ax.set_ylim(0, max_rand)
ax.set_xlim(0, max_x-1)
line, = ax.plot(x, np.random.randint(0, max_rand, max_x))
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{:.0f}s'.format(max_x - x - 1)))
plt.xlabel('Seconds ago')

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=10, blit=True, save_count=10)

plt.show()

# ser = serial.Serial(port=serial_ports()[1], baudrate=115200, bytesize=8, 
#                     parity='N', stopbits=1, timeout=0.1, 
#                     xonxoff=0, rtscts=0)


#         # Check if the message is already finished
# while not out.endswith('[3;05f'):
# # Save the last received characters
# # A `bytes` object is encoded in 'ISO-8859-1'
# received_chars = str(ser.read(), 'ISO-8859-1')
# if received_chars == 'þ':
#     received_chars = ''
# if received_chars == '':
#     received_chars = '\n'

# # Add them to `out`
# out += received_chars
            
# # Find data index
# index = out.rfind('[3;05f')
# if index != -1:
#     result = out[index-4:index]
#     data = int(result)

plt.show()

# ser.close()