import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5001))
sock.listen(2)

print("Device2 is running...")

conn, addr = sock.accept()
print("Connected with", addr)

while True:
  msg = conn.recv(1024).decode()
  if not msg:
    break

  if msg == 'Request':
    heart = random.randint(40, 140)
    step = random.randint(2000, 6000)
    cal = random.randint(1000, 4000)

    data = f"Heartbeat={heart}, Steps={step}, Cal={cal}"
    conn.sendall(data.encode())

  elif msg == 'quit':
    break

conn.close()
sock.close()
