from socket import *
serverIP = "127.0.1.1"
serverPort = 5120
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect((serverIP, serverPort))
    print "\nConnection Successful!"
    filename = "wrongname.txt"
    clientSocket.send("GET /" + filename + " HTTP/1.1\r\n" +
                      "Host: " + gethostbyname(gethostname()) + ":" + str(clientSocket.getsockname()[1]) + "\r\n\r\n")
    print "\n\n---------------HTTP RESPONSE---------------\n"
    response = clientSocket.recv(1024)
    print response
    fileData = clientSocket.recv(10000)
    print fileData
    print "---------------END OF HTTP RESPONSE---------------\n"
    clientSocket.close()

except error:
    print "\n\nError while connecting!"
    clientSocket.close()
