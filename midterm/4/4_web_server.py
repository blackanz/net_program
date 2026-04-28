import socket


def res():
  c.send(b'HTTP/1.1 200 OK\r\n')
  c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
  c.send(b'\r\n')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
  c, addr = s.accept()
  data = c.recv(1024)
  msg = data.decode()
  req = msg.split('\r\n')
  url = req[0].split()[1]
  path = url.lstrip('/')

  if path.startswith('midterm?name='):
    p = url.lstrip('&id=')
    mimeType = 'text/html; charset=utf-8'
    res()
    name = p[0].split('=')[1]
    id = p[0].split('&=')[1]
    # c.send(b'<HTML><BODY><H1>Hello, ' + name.encode() +
    #        b'! Your ID is ' + id.encode() + b'</H1></BODY></HTML>')
    response = f'<HTML><BODY><H1>Hello, {name}! Your ID is</H1></BODY></HTML>'
    c.send(response)
    continue

  elif path.endswith('.html'):  # index.html 요청
    with open(path, 'r', encoding='utf-8') as f:
      print('Html ', addr)
      mimeType = 'text/html; charset=utf-8'
      data = f.read()
      res()
      c.send(data.encode())
      continue

  elif path.endswith('.png'):  # iot.png 요청
    with open(path, 'rb') as f:
      print('Png', addr)
      mimeType = 'image/png'
      data = f.read()
      res()
      c.send(data)
      continue

  elif path.endswith('.ico'):  # favicon.ico 요청
    with open(path, 'rb') as f:
      print('Ico', addr)
      mimeType = 'image/x-icon'
      data = f.read()
      res()
      c.send(data)
      continue

  else:  # 이외 모든 경우
    print('Unknown', addr)
    c.send(b'HTTP/1.1 404 Not Found\r\n')
    c.send(b'\r\n')
    c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
    c.send(b'<BODY>Not Found</BODY></HTML>')
    c.close()
