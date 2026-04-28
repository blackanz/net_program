import socket

port = 5000
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost', port))
sock.settimeout(1)

while True:
  msg = input('-> ')
  reTx = 0

  if msg == 'quit':
    sock.send(msg.encode())
    break

  while reTx <= 3:
    try:
      sock.send(msg.encode())
      data = sock.recv(BUFFSIZE)
      print(data.decode())

    except socket.timeout:
      reTx += 1
      continue

    else:
      print("Failed: No response")

sock.close()
