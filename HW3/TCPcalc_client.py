import socket

addr = ('localhost', 2500)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(addr)

  while True:
    msg = input("Enter expression. 'q' to exit:\n")
    if msg == 'q':
      s.sendall(msg.encode())
      print('End the process...')
      break

    s.sendall(msg.encode())
    try:
      data = s.recv(1024)
      if not data:
        break
      result = data.decode()
      try:
        float(result)
        print('Result: ', result)
      except:
        print(result)
    except:
      print('Error')
