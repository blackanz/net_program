import socket
import struct

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(('localhost', 5050))
  s.sendall(b'Hello')
  data = s.recv(12)
  sid, rid, lumi, humi, temp, air, seq = struct.unpack("!HHBBBBI", data)
  print(
      f"Sender:{sid}, Receiver:{rid}, "
      f"Lumi:{lumi}, Humi:{humi}, Temp:{temp}, Air:{air}, Seq:{seq}"
  )
