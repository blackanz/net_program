import socket
import random

BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 5000))
sock.connect(('localhost', 5000))

while True:
  sock.settimeout(None)
  while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    if random.random() <= 0.3:
      continue
    else:
      sock.send(b'ack')
      print('<-', data.decode())

    sock.close()
