import datetime
import os


def respond_request(data_link):
    filename = './public'
    if data_link[1] == '/':
        filename += '/index.html'
    else:
        filename += data_link[1]
    extension = os.path.splitext(filename)

    if extension[1] == '.html':
        contentType = "text/html"
    elif extension[1] == '.css':
        contentType = "text/html"
    elif extension[1] == '.pnj':
        contentType = "image"
    elif extension[1] == 'jpg':
        contentType = "image"

    try:
        file = open(filename, "r")
        data = file.read()
        respond = 'HTTP/1.1 200 OK\r\n'
        respond += 'Content-Length: ' + str(len(data)) + '\r\n'
        respond += 'Connection: close\r\n'
        respond += 'Content-Type: ' + contentType + '\r\n\r\n'
        respond += data
    except IOError:
        file = open('./public/404.html', "r")
        data = file.read()
        respond = 'HTTP/1.1 404 Not Found\r\n'
        respond += 'Content-Length: ' + str(len(data)) + '\r\n'
        respond += 'Connection: close\r\n'
        respond += 'Content-Type: text/html\r\n\r\n'
        respond += data
    return respond




