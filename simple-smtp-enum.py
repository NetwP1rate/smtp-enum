#!/usr/bin/python

import socket,sys

if len(sys.argv) != 3:
  print("[-] Please give 3 arguments\n")
  sys.exit(0)
  
ip = sys.argv[1]
port = 25
user = sys.argv[2]

s = socket.socket(socket.AF_INE, socket.SOCK_STREAM)

connect = s.connect((ip,port))
banner = s.recv(1024)

if '220' in str(banner):
  s.send((f"VRFY {user}\r\n").encode())
  print(f"User" [{user}] found!)
  
s.close()
