from socket import * 

serverName = 'localhost' 
serverPort = 12000 
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 

x = input("Insira um valor numerico X:") 
clientSocket.send(x.encode()) 
response = clientSocket.recv(1024) 

print(x,'² = ', response) 
clientSocket.close() 







