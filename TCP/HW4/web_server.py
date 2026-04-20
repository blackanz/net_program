import socket


def res():
  f.close()
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
  filename = req[0].split()[1].lstrip('/')

  if filename.endswith('.html'):  # index.html 요청
    with open(filename, 'r', encoding='utf-8') as f:
      print('Html ', addr)
      mimeType = 'text/html; charset=utf-8'
      data = f.read()
      res()
      c.send(data.encode())

  elif filename.endswith('.png'):  # iot.png 요청
    with open(filename, 'rb') as f:
      print('Png', addr)
      mimeType = 'image/png'
      data = f.read()
      res()
      c.send(data)

  elif filename.endswith('.ico'):  # favicon.ico 요청
    with open(filename, 'rb') as f:
      print('Ico', addr)
      mimeType = 'image/x-icon'
      data = f.read()
      res()
      c.send(data)

  else:  # 이외 모든 경우
    print('Unknown', addr)
    c.send(b'HTTP/1.1 404 Not Found\r\n')
    c.send(b'\r\n')
    c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
    c.send(b'<BODY>Not Found</BODY></HTML>')
    c.close()
