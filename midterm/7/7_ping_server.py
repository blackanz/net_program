import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
  s.bind(('localhost', 7777))
  s.listen(3)
  conn, addr = s.accept()
  s.settimeout(1)

  while True:
    data = conn.recv(1024)

    if not data:
      break

    msg = data.decode()

    if msg == 'ping':
      conn.sendall('pong'.encode())

  conn.close()
