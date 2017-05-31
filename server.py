import socket,subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 80))
s.listen(1)
print("Start Listen Server")
con, address = s.accept()
print(address)
while True:
    data = con.recv(1024)
    if not data:
        break
    print("Message from Client data : %s" % data.decode())
    msg = data.decode()

    if (msg == 'quit') :
        break
    elif (msg == 'stop') :
        break
    con.send(msg.encode())
    subprocess.call(msg)
s.close()