import socket
import struct

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(('localhost', 5050))
  s.sendall(b'Hello')
  data = s.recv(12)
  length, lumi, humid, temp, air, ip, vard = struct.unpack(
      "!HBBBBss", data)
  print(
      f"Length:{length}, Lumi:{lumi}, Humi:{humid}, Temp:{temp}, Air:{air}, IP:{ip}, Variable Data: {vard}"
  )
