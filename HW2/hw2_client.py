import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

# 이름 전송
sock.send(b'Naeun Kim')

# 학번 수신
id_b = sock.recv(4)
id = int.from_bytes(id_b, 'big')
print(id)

sock.close()
