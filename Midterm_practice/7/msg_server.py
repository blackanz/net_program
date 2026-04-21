import socket
import random

port = 5000
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

mailbox = {}

print("Server started...")

while True:
  data, addr = sock.recvfrom(BUFFSIZE)
  msg = data.decode().strip()

  if msg == "quit":
    break

  parts = msg.split()

  if parts[0] == "send":
    if random.randint(1, 100) <= 25:
      print('Packet from {} lost!'.format(addr))
      continue

    mboxID = parts[1]
    msg = ' '.join(parts[2:])

    if mboxID not in mailbox:
      mailbox[mboxID] = []

    mailbox[mboxID].append(msg)
    sock.sendto("OK".encode(), addr)

  elif parts[0] == "receive":
    if random.randint(1, 100) <= 25:
      print('Packet from {} lost!'.format(addr))
      continue

    mboxID = parts[1]

    if mboxID in mailbox and len(mailbox[mboxID]) > 0:
      msg = mailbox[mboxID].pop(0)

    else:
      msg = "No message"

    sock.sendto(msg.encode(), addr)

sock.close()
