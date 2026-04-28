import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8000))
sock.listen(1)

while True:
  c, addr = sock.accept()
  if sock.recv() == 'quit':
    continue

  sock.close()
