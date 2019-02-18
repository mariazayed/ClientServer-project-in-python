import socket


def reversed_string(string):
    str = string[::-1]
    str = str.swapcase()
    return str


BUFFER_SIZE = 1024
PORT = 300
HOST = '192.168.1.112'

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print('Listening to {}'.format(server_socket.getsockname()))

while True:
    data, client_address = server_socket.recvfrom(BUFFER_SIZE)
    msg = data.decode('ascii')
    print('Client''s address {}'.format(client_address))
    rev_msg = reversed_string(msg)
    data = rev_msg.encode('ascii')
    server_socket.sendto(data, client_address)
