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
  # filename = req[0].split()[1].lstrip('/')
  url = req[0].split()[1]
  path = url.lstrip('/')
  filename = path

  if path.startswith('exam?q='):
    mimeType = 'text/html; charset=utf-8'
    res()
    p = path.split('=')[1]
    response = b'<HTML><BODY>Hello, ' + p.encode() + b'</BODY></HTML>'
    c.send(response)
    c.close()

  elif filename.endswith('.html'):  # index.html 요청
    with open(filename, 'r', encoding='utf-8') as f:
      print('Html ', addr)
      mimeType = 'text/html; charset=utf-8'
      data = f.read()
      res()
      c.send(data.encode())
      c.close()

  elif filename.endswith('.png'):  # iot.png 요청
    with open(filename, 'rb') as f:
      print('Png', addr)
      mimeType = 'image/png'
      data = f.read()
      res()
      c.send(data)
      c.close()

  elif filename.endswith('.ico'):  # favicon.ico 요청
    with open(filename, 'rb') as f:
      print('Ico', addr)
      mimeType = 'image/x-icon'
      data = f.read()
      res()
      c.send(data)
      c.close()

  else:  # 이외 모든 경우
    print('Unknown', addr)
    c.send(b'HTTP/1.1 404 Not Found\r\n')
    c.send(b'\r\n')
    c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
    c.send(b'<BODY>Not Found</BODY></HTML>')
    c.close()
