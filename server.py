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
    data = str(connection.recv(8192))

    components = data.split(" ")
    respond = ""
    if components[0] == "b'GET":
        respond = get.respond_request(components)
    elif components[0] == "b'POST":
        respond = post.respond_request(components)
    else:
        connection.sendall(bytes(""))

    try:
        connection.sendall(respond)
    except TypeError:
        print(respond)
    connection.close()
