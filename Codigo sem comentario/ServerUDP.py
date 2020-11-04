from socket import * 

serverPort = 12001 
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Servidor pronto! Aguardando um valor numerico')

while 1:
    valor, addr = serverSocket.recvfrom(2048)
    print('Valor recebido do cliente', addr, ': ', valor)

    try:
        valor = int(valor)
        valorAoQuadrado = str(valor * valor)
        pass
    except (Exception), e:
        valorAoQuadrado = "Insira apenas valores inteiros (numericos), por favor!"

    serverSocket.sendto(valorAoQuadrado, addr)
