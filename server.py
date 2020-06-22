import socket
import get
import post

host = '127.0.0.1'
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
# Allow 10 people in pending room
s.listen(10)

print("Listening at", s.getsockname())

while True:
    connection, address = s.accept()
    data = connection.recv(8192)


