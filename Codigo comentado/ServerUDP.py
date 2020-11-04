from socket import * #Importacao da biblioteca SOCKET, o asteritico (*) representa que quero todas as funcionalidades

serverPort = 12001 #Definindo uma variavel que contera o numero da porta utilizada pelo servidor
serverSocket = socket(AF_INET, SOCK_DGRAM) #Definindo a conexao socket, onde
#AF_INET = Familia de enderecos que o socket pode se comunicar, neste caso, enderecos em uma rede com protocolo IPV4
#SOCK_DGRAM = Explicitando que queremos um DATAGRAMA, ou seja, utilizaremos o protocolo UDP
serverSocket.bind(('', serverPort))#realizando BIND do nome_do_servidor:porta
print('Servidor pronto! Aguardando um valor numerico')#Mensagem para avisar que o servidor está rodando

while 1: #Loop infinito
    valor, addr = serverSocket.recvfrom(2048) #Recupera a mensagem e o endereço conectado
    print('Valor recebido do cliente', addr, ': ', valor)

    try: #tratamento de erro
        valor = int(valor) #converte o valor para inteiro pois vem como string (texto)
        valorAoQuadrado = str(valor * valor) #Realiza a elevação do valor e o converte para STRING (pois o servidor retorna mensagens)
        pass
    except (Exception), e:#Caso seja passado um valor diferente de um valor numérico, o servidor retornara a mensagem de erro:
        valorAoQuadrado = "Insira apenas valores inteiros (numericos), por favor!"

    serverSocket.sendto(valorAoQuadrado, addr) #Servidor envia a mensagem para o endereco, neste caso, o endereco que foi recuperado na linha 11
