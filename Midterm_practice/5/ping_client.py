import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
  s.connect(('localhost', 7000))

  for i in range(3):
    s.sendall('ping'.encode())
    start = time.time()
    data = s.recv(1024)
    end = time.time()

    if data.decode() == 'pong':
      rtt = end - start
      print(f"Success (RTT: {rtt:.6f})")
