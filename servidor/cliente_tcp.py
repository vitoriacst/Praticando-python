from socket import *
from urllib import response

servidor ='127.0.1'
porta=43210

msg = bytes(input('digite algo: '),"utf-8")
obj_socket = socket(AF_INET,SOCK_STREAM)
obj_socket.connect((servidor,porta))
obj_socket.send(msg)
resposta = obj_socket.recv(1024)
print("recebemos: ", resposta)
obj_socket.close()
