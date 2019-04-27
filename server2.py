from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', 80))
serverSocket.listen()

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = str(connectionSocket.recv(4096), encoding='utf-8') 
        if not message:
            connectionSocket.close()
            continue

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() 
        outputdata_bytes = bytes(outputdata, encoding='gb18030')

        headers = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\nContent-Length: {}\n\n'.format(len(outputdata_bytes))
        connectionSocket.send(bytes(headers, encoding='utf-8'))
  
        connectionSocket.send(outputdata_bytes)
        connectionSocket.close()
    except IOError:
       
        outputdata_bytes = bytes('Not Found', encoding='utf-8')
        headers = 'HTTP/1.1 404 Not Found\nContent-Type: text/html; charset=utf-8\nContent-Length: {}\n\n'.format(len(outputdata_bytes))
        connectionSocket.send(bytes(headers, encoding='utf-8'))
        connectionSocket.send(outputdata_bytes)

        connectionSocket.close()
serverSocket.close()
