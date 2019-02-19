import socket

HOST = 'localhost'
PORT = 300
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = input("Input message:")
client_socket.send(message.encode('ascii'))

data = client_socket.recv(BUFFER_SIZE)
print('The SERVER replies : {}'.format(data.decode('ascii')))
client_socket.close()
