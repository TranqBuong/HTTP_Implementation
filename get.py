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
    file=open("./public/index.html","r")
    data = file.read()
    respond +='Content-Length: '+str(len(data))+'\r\n'
    respond += 'Connection: close\r\n'
    respond += 'Content-Type: text/html\r\n\r\n'
    respond += data

    return respond
