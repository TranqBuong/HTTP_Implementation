
def respond_request(request):

    if request[1] == '/signin':
        req = request[-1].splitlines()
        print(req)
        if req[-1] == 'username=admin&password=admin':
            file = open('./public/info.html','rb')
            data = file.read()
            respond = 'HTTP/1.1 301 Moved Permanently\r\n'
        else :
            file = open('./public/404.html', "rb")
            data = file.read()
            respond = 'HTTP/1.1 404 Not Found\r\n'

    return respond












