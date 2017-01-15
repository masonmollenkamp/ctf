# Echo client program
import socket

HOST =  "jared"   # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Mason')
data = s.recv(2)
s.close()
print 'Received', repr(data)
