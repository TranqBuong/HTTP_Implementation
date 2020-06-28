
def respond_request(request_headers):

    if request_headers[1] == '/signin':

        req = request_headers[-1].split('\\r\\n\\r\\n')

        req[-1] = req[-1].replace("'","")

        if req[-1] == 'username=admin&password=admin':
            respond = 'HTTP/1.1 301 Moved Permanently\r\n'
            respond += "Location: info.html"

        else :
            respond = 'HTTP/1.1 301 Moved Permanently\r\n'
            respond += "Location: 404.html"

    respond = bytes(respond, "utf-8")

    return  respond












