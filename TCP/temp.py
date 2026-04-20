import socket

PORT = 2500
BUFSIZE = 1024


def calc(expr):
  expr = expr.replace(' ', '')
  ops = ['+', '-', '*', '/']
  op = None

  for ch in expr:
    if ch in ops:
      op = ch
      break

  if op is None:
    return 'Error'

  a, b = expr.split(op, 1)

  try:
    x = int(a)
    y = int(b)
  except:
    return 'Error'

  try:
    if op == '+':
      return str(x + y)
    elif op == '-':
      return str(x - y)
    elif op == '*':
      return str(x * y)
    elif op == '/':
      return f'{x / y:.1f}'
  except ZeroDivisionError:
    return 'Error: Division by zero'

  return 'Error'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind(('', PORT))
  s.listen(5)
  print('Calculator server is running...')

  while True:
    conn, addr = s.accept()
    with conn:
      print('connected by', addr)
      while True:
        data = conn.recv(BUFSIZE)
        if not data:
          break

        msg = data.decode().strip()
        if msg == 'q':
          break

        result = calc(msg)
        conn.sendall(result.encode())
