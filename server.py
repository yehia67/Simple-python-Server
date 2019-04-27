
from socket import  *
import threading
def main():
    serverPort=81
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print ('the web server is running on port:',serverPort)
    while True:
          print ('Ready to serve...')
          connectionSocket, addr = serverSocket.accept()
          try:
              message = connectionSocket.recv(1024)
              print(message,'::',message.split()[0],':',message.split()[1])
              filename = message.split()[1]
              print(filename,'||',filename[1:])
              f = open(filename[1:])
              outputdata = f.read()
              print(outputdata)
              connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
              connectionSocket.send(outputdata)
              for i in range(0, len(outputdata)):
                   connectionSocket.send(outputdata[i])
                   connectionSocket.close()
          except IOError:
               connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
               connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n') 
               connectionSocket.close()
     
          serverSocket.close()     
main()
