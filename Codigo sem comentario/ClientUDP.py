from socket import * 

serverName = 'localhost' 
serverPort = 12001 
clientSocket = socket(AF_INET, SOCK_DGRAM) 
clientSocket.connect((serverName, serverPort)) 

x = input("Insira um valor numerico X:") 
clientSocket.send(x.encode()) 
response = clientSocket.recv(2048) 

print(x,'² = ', response) 
clientSocket.close() 







