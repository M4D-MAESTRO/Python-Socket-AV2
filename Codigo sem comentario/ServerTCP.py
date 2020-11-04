from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Servidor pronto! Aguardando um valor numerico')

while 1:
    connectionSocket, addr = serverSocket.accept()
    valor = connectionSocket.recv(1024)
    print('Valor recebido do cliente', addr, ': ', valor)

    try:
        valor = int(valor)
        valorAoQuadrado = str(valor * valor)
        pass
    except (Exception), e:
        valorAoQuadrado = "Insira apenas valores inteiros (numericos), por favor!"

    connectionSocket.send(valorAoQuadrado)
    connectionSocket.close()
