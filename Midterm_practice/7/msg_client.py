import socket

port = 5000
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost', port))
sock.settimeout(1)

while True:
  msg = input('Enter the message ("send mboxId message" or "receive mboxId"): ')

  if msg == 'quit':
    sock.send(msg.encode())
    break

  reTx = 0

  while reTx <= 2:
    try:
      sock.send(msg.encode())
      data = sock.recv(BUFFSIZE)
      print(data.decode())

    except socket.timeout:
      reTx += 1
      print("Timeout retry")
      continue

    else:
      print("Failed: No response")

sock.close()
