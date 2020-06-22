import datetime

def respondRequest(data):
    respond = 'HTTP/1.1 200 OK\r\n'
    respond +='Date: '
    respond += datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT\r\n")
    respond +='Server: local host\r\n'
    respond +='Last-Modified: '
    respond +='Mon, 22 Jun 2020 22:00 GMT\r\n'
    respond +='Accept-Ranges: '
    respond +='bytes\r\n'
    respond +="Status: 200\r\n"
    respond +='Content-Length: 12\r\n'
    respond += 'Connection: close\r\n'
    respond += 'Content-Type: text/html\r\n\r\n'
    respond +='Hello world'
    return respond