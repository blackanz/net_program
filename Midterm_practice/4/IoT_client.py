import socket

BUFF_SIZE = 1024
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', port))

while True:
  for msg in ['1', '2', '3']:
    s.send(msg.encode())
    data, addr = s.recvfrom(BUFF_SIZE)

    t = int.from_bytes(data[0:2], 'big')
    h = int.from_bytes(data[2:4], 'big')
    l = int.from_bytes(data[4:6], 'big')

    print(f"Temp={t}, Humid={h}, Lumi={l}")
