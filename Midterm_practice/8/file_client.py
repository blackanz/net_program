import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect('localhost', 6789)

# 1. Hello 전송
sock.send("Hello".encode())

# 2. Filename 요청 수신
data, _ = sock.recvfrom(4096)
if data.decode() != "Filename":
  print("Protocol error")
  exit()

# 3. 파일 이름 입력 및 전송
filename = input("Enter filename: ")
sock.send(filename.encode())

# 4. 파일 또는 NOFILE 수신
data, _ = sock.recvfrom(65535)

if data.startswith(b"NOFILE"):
  print("File not found on server")
  sock.send("Bye".encode())
  sock.close()
  exit()

# 5. 파일 저장
if data.startswith(b"FILE|"):
  file_content = data.split(b"|", 1)[1]

  with open("received_" + filename, "wb") as f:
    f.write(file_content)

  print("File received successfully")

# 6. 종료 메시지
sock.send("Bye".encode())

sock.close()
