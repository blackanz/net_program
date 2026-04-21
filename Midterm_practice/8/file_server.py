import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind('localhost', 6789)

print("Server started...")

while True:
  # 1. Hello 수신
  data, addr = sock.recvfrom(4096)
  if data.decode() != "Hello":
    continue

  print('Client connected', addr)

  # 2. Filename 요청
  sock.sendto("Filename".encode(), addr)

  # 3. 파일명 수신
  filename, addr = sock.recvfrom(4096)
  filename = filename.decode()

  print('Requested file', filename)

  # 4. 파일 존재 여부 확인
  if not os.path.exists(filename):
    sock.sendto("NOFILE".encode(), addr)
    continue

  # 파일 읽기
  with open(filename, "rb") as f:
    file_data = f.read()

  message = b'FILE|' + file_data

  # 5. 재전송 로직 (최대 3회, 2초 대기)
  sock.settimeout(2)

  for attempt in range(3):
    print("Send attempt", attempt + 1)
    sock.sendto(message, addr)

    try:
      ack, addr = sock.recvfrom(4096)
      if ack.decode() == "Bye":
        print("Client acknowledged (Bye received)")
        break
    except socket.timeout:
      print("Timeout, retransmitting...")

  sock.settimeout(None)
