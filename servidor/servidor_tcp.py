from socket import *

servidor ='127.0.1'
porta=43210

obj_socket = socket(AF_INET,SOCK_STREAM)
obj_socket = socket.bind((servidor,porta))
obj_socket.listen(2)

print("aguardando cliente. . . .")

while True:
  con, client = obj_socket.accept()
  print("Conectando com: ", client)
  while True:
    msg_recebida = str(con.recv(1024))
    print("Recebi", msg_recebida)
    msg_enviada =b'teste'
    con.send(msg_enviada)
    break
  con.close()
