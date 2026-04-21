import socket
import struct
import random


def pack_app():
  sid = random.randint(1, 50000)
  rid = random.randint(1, 50000)

  lumi = random.randint(1, 100)
  humid = random.randint(1, 100)
  temp = random.randint(1, 100)
  air = random.randint(1, 100)

  seq = random.randint(1, 100000)

  packed = struct.pack(
      "!HHBBBBI",
      sid, rid, lumi, humid, temp, air, seq
  )
  return packed


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind(('', 5050))
  s.listen(1)

  while True:
    conn, addr = s.accept()
    data = conn.recv(1024).decode()

    if data == 'Hello':
      packed = pack_app()
      conn.sendall(packed)

    conn.close()
