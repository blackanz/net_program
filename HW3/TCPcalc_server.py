import socket

PORT = 2500
ops = ['+', '-', '*', '/']


def calc(exp):
  exp = exp.replace(' ', '')
  op = None

  for char in exp:
    if char in ops:
      op = char
      break

  if op is None:
    return 'No operator'

  try:
    a, b = exp.split(op, 1)
    x = int(a)
    y = int(b)
  except:
    return 'Invalid number!'

  try:
    if op == '+':
      return str(x+y)
    elif op == '-':
      return str(x-y)
    elif op == '*':
      return str(x*y)
    elif op == '/':
      return f'{x/y:.1f}'
  except ZeroDivisionError:
    return "Can't divide by zero!"
  return 'Fail to calculate'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind(('', PORT))
  s.listen(1)
  print('Waiting for connection...')

  while True:
    client, addr = s.accept()
    print('Connection from ', addr)

    while True:
      data = client.recv(1024)
      if not data:
        print('Client disconnected')
        break

      msg = data.decode().strip()

      if msg == 'q':
        print('Client disconnected')
        break

      result = calc(msg)
      client.sendall(result.encode())

    client.close()
