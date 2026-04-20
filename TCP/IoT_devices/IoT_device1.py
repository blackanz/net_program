import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5000))
sock.listen(2)

print("Device1 is running...")

conn, addr = sock.accept()
print("Connected with", addr)

while True:
  msg = conn.recv(1024).decode()
  if not msg:
    break

  if msg == 'Request':
    temp = random.randint(0, 40)
    humid = random.randint(0, 100)
    lumin = random.randint(70, 150)

    data = f"Temp={temp}, Humid={humid}, Iilum={lumin}"
    conn.sendall(data.encode())

  elif msg == 'quit':
    break

conn.close()
sock.close()
