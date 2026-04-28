import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
  s.connect(('localhost', 7777))
  reTx = 0

  while reTx <= 2:
    try:
      s.send(data.encode())
      data = s.recv(1024)
      print(data.decode())

      for i in range(2):
        s.sendall('ping'.encode())
        start = time.time()
        data = s.recv(1024)
        end = time.time()

        if data.decode() == 'pong':
          rtt = end - start
          print(f"Success (RTT: {rtt:.6f})")

    except socket.timeout:
      reTx += 1
      print("Timeout retry")
      continue

    else:
      print("Failed: No response")
