import os
image_extensions = ['.png', '.jpg', '.jpeg', '.ico']

def respond_request(request_url):
    filename = './public'
    if request_url == '/':
        filename += '/index.html'
    else:
        filename += request_url

    extension = os.path.splitext(filename)

    content_type = "document"

    if extension[1] == '.html':
        content_type = "text/html"
    elif extension[1] == '.css':
        content_type = "text/css"
    elif extension[1] in image_extensions:
        content_type = "image/" + extension[1][1:]

    try:
        file = open(filename, "rb")
        data = file.read()
        respond = 'HTTP/1.1 200 OK\r\n'
    except IOError:
        file = open('./public/404.html', "rb")
        data = file.read()
        respond = 'HTTP/1.1 404 Not Found\r\n'
        content_type = 'text/html'

    respond += 'Content-Length: ' + str(len(data)) + '\r\n'
    respond += 'Connection: close\r\n'
    respond += 'Content-Type: ' + content_type + '\r\n\r\n'
    respond = bytes(respond, "utf-8")
    respond += data
    return respond




