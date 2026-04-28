import socket
import struct
import random


def pack_app():
  lumi = random.randint(1, 100)
  humid = random.randint(1, 100)
  temp = random.randint(1, 100)
  air = random.randint(1, 100)

  for vard in range(random.randint(1, 10)):
    print("*")

  l = lumi + humid + temp + air + vard
  length = len(l).to_bytes(2, 'big')
  ip = b'1'

  packed = struct.pack(
      "!HBBBBss",
      length, lumi, humid, temp, air, ip, vard
  )
  return packed


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind(('localhost', 5050))
  s.listen(1)

  while True:
    conn, addr = s.accept()
    data = conn.recv(1024).decode()

    if data == 'Hello':
      packed = pack_app()
      conn.sendall(packed)

    conn.close()
