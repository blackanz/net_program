import socket

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
  c, addr = s.accept()

  data = c.recv(1024)
  msg = data.decode()
  req = msg.split('\r\n')
