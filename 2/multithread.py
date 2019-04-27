from socket import *
from threading import Thread


def serviceRequest(connectionSocket):
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        print '\n\n-------------------------------------------------'
        print "Request for file " + filename[1:]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
        connectionSocket.send(outputdata)
        connectionSocket.close()

    except IOError:  
      headers = 'HTTP/1.1 404 Not Found\nContent-Type: text/html; charset=utf-8\nContent-Length: {}\n\n'
      connectionSocket.send(headers)
      connectionSocket.close()
    except IndexError:
        connectionSocket.close()



serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((gethostname(), 5120))
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
print "\nServer has been started at IP = " + gethostbyname(gethostname()) + " and port = 80"
threads = []

while True:
    serverSocket.listen(40)
    connectionSocket, address = serverSocket.accept()
    newThread = Thread(target=serviceRequest, args=(connectionSocket,))
    newThread.start()
    threads.append(newThread)

serverSocket.close()
