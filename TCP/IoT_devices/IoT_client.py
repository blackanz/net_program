import socket
import time

d1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
d1.connect(('localhost', 5000))

d2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
d2.connect(('localhost', 5001))

f = open('data.txt', 'a')
print("1: Device1, 2: Device2, quit: 종료")

while True:
  cmd = input(">> ")
  if cmd == "1":
    d1.send(b'Request')
    data = d1.recv(1024).decode()
    now = time.ctime()
    inf = f"{now}: Device1: {data}"
    print(inf)
    f.write(inf + '\n')

  elif cmd == "2":
    d2.send(b'Request')
    data = d2.recv(1024).decode()
    now = time.ctime()
    inf = f"{now}: Device2: {data}"
    print(inf)
    f.write(inf + '\n')

  elif cmd == 'quit':
    d1.send(b'quit')
    d2.send(b'quit')
    break

  else:
    print("Wrong input. Try again")

f.close()
d1.close()
d2.close()
