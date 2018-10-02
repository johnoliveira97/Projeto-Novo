import socket
import os
import stat

host = '127.0.0.1'  
port = 5000      

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
envio = (host,port)
tcp.connect(envio)
 
print('Digite: S e pressione ENTER para encerrar...') 
print('DIGITE A MENSAGEM: ')
mensagem = input()
 
while mensagem not in ('s','S'):
    tcp.send(str(mensagem).encode())
    mensagem = input()
 
tcp.close()