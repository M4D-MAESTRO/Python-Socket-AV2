from socket import * #Importacao da biblioteca SOCKET, o asteritico (*) representa que quero todas as funcionalidades

serverName = 'localhost' #Definindo uma variavel que contera o nome do servidor
serverPort = 12001 #Definindo uma variavel que contera o numero da porta utilizada pelo servidor
clientSocket = socket(AF_INET, SOCK_DGRAM) #Definindo a conexao socket, onde
#AF_INET = Familia de enderecos que o socket pode se comunicar, neste caso, enderecos em uma rede com protocolo IPV4
#SOCK_DGRAM = Explicitando que queremos um DATAGRAMA, ou seja, utilizaremos o protocolo UDP
clientSocket.connect((serverName, serverPort)) #Realizando a conexao no nome_do_servidor:porta

x = input("Insira um valor numerico X:") #Requisitando um INPUT para o usuario de um valor numerico
clientSocket.send(x.encode()) #Enviando uma requisicao para o servidor com o valor ENCODADO
response = clientSocket.recv(2048) #Recuperacao da resposta do servidor

print(x,'² = ', response) #Print da resposta
clientSocket.close() #Fechando conexao







