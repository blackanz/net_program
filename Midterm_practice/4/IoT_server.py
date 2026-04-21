import socket
import random

BUFF_SIZE = 1024
port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', port))

print("Device is running...")

while True:
  data, addr = sock.recvfrom(BUFF_SIZE)
  msg = data.decode()
  temp, humid, lumin = 0, 0, 0

  if msg == '1':
    temp = random.randint(1, 50)
  elif msg == '2':
    humid = random.randint(1, 100)
  elif msg == '3':
    lumin = random.randint(1, 150)

  res = (temp.to_bytes(2, 'big') +
         humid.to_bytes(2, 'big') +
         lumin.to_bytes(2, 'big'))

  sock.sendto(res, addr)
