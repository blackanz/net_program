import socket

port = 4000
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

mailbox = {}

print("Server started...")

while True:
  data, addr = sock.recvfrom(BUFFSIZE)
  msg = data.decode().strip()

  if msg == "quit":
    print("Server shutting down...")
    break

  parts = msg.split()

  if parts[0] == "send":
    mboxID = parts[1]
    message = ' '.join(parts[2:])

    if mboxID not in mailbox:
      mailbox[mboxID] = []

    mailbox[mboxID].append(message)
    sock.sendto("OK".encode(), addr)

  elif parts[0] == "receive":
    mboxID = parts[1]

    if mboxID in mailbox and len(mailbox[mboxID]) > 0:
      message = mailbox[mboxID].pop(0)
      sock.sendto(message.encode(), addr)
    else:
      sock.sendto("No messages".encode(), addr)

sock.close()
