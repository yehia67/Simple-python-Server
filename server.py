from socket import  *
def main():
    serverPort=80
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print ('the web server is running on port:',serverPort)
    while True:
          print('Ready to serve...')
          connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print(message,'::',message.split()[0],':',message.split()[1])

      
