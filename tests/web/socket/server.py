#SERVER (Сервер)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
sock = socket.socket()
sock.bind(('', 9090)) #Хост любой, порт 9090
sock.listen(1) #Не более 1 клиента

#Принять информацию от клиента. conn - новый 
#сокет; addr - адрес клиента:
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024) #Получаем информацию порциями по 1024 bytes
    if not data:
        break
    conn.send(data.upper()) #Вернуть клиенту строку в верхнем регистре

conn.close()
