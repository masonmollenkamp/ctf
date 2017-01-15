# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
mason = 0
jared = 0
while 1:
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(5)
    if (data=="Mason"):
        mason = mason + 1
    if (data=="Jared"):
        jared = jared + 1
    if (data=="dones"):
        break  
    conn.send('ok');
print ("Mason: " + str(mason))
print ("Jared: " + str(jared))

