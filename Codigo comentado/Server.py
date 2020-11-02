from socket import * #Importação da biblioteca SOCKET, o asterítico (*) representa que quero todas as funcionalidades

serverPort = 12000 #Definindo uma variável que conterá o número da porta utilizada no servidor
serverSocket = socket(AF_INET, SOCK_STREAM)#Definindo a conexão socket, onde
#AF_INET = Familia de endereços que o socket pode se comunicar, neste caso, endereços em uma rede com protocolo IPV4
#SOCK_STREAM = Explicitando que queremos um fluxo (Stream), ou seja, uma sequencia de caracteres usando o protocolo TCP
serverSocket.bind(('', serverPort)) #realizando BIND do nome_do_servidor:porta
serverSocket.listen(1) #Colocando o socket para ficar ouvindo as requisições
print('Servidor pronto! Aguardando um valor numerico') #Mensagem para avisar que o servidor está rodando

while 1: #Loop infinito
    connectionSocket, addr = serverSocket.accept() #Recupera a conexão e o cliente conectado

    try: #tratamento de erro
        valor = int(connectionSocket.recv(1024)) #Recupera o valor passado pelo cliente e já o converte para INTEIRO
        valorAoQuadrado = str(valor * valor) #Realiza a elevação do valor e o converte para STRING (pois o servidor retorna mensagens)
        pass
    except (Exception), e: #Caso seja passado um valor diferente de um valor numérico, o servidor retornara a mensagem de erro:
        valorAoQuadrado = "Insira apenas valores inteiros (numericos), por favor!"

    connectionSocket.send(valorAoQuadrado) #Servidor responde o cliente
    connectionSocket.close() #Servidor encerra aquela conexão


