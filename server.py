import socket
import get
import post

host = '127.0.0.1'
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
# Allow 10 people in waiting room
s.listen(10)

print("Listening at ", s.getsockname()[0], ":", s.getsockname()[1], sep="")

while True:
    connection, address = s.accept()
    request_headers = connection.recv(8192).decode().split("\r\n")

    top_header = request_headers[0].split(" ")
    if top_header[0] == "GET":
        respond = get.respond_request(top_header[1])
    elif top_header[0] == "POST":
        request_body = request_headers[-1]
        respond = post.respond_request(top_header, request_body)
    else:
        respond = bytes("", "UTF-8")

    connection.sendall(respond)
    connection.close()
