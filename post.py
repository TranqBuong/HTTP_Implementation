def respond_request(top_header, request_body):
    if top_header[1] == '/signin':
        if request_body == 'username=admin&password=admin':
            respond = 'HTTP/1.1 301 Moved Permanently\r\n'
            respond += "Location: info.html"
        else:
            respond = 'HTTP/1.1 301 Moved Permanently\r\n'
            respond += "Location: 404.html"
    else:
        respond = ""

    respond = bytes(respond, "utf-8")
    return respond
