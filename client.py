import sys, socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("zaeval.ga", 80))
while True:
   msg = input("입력 : ")
   s.sendall(msg.encode())
   data = s.recv(1024)
   if not data:
      break
   print("Echo from Server Data : %s" % data.decode())
s.close()

