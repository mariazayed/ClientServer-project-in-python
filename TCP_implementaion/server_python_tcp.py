import socket


def reversed_string(string):
    str = string[::-1]
    str = str.swapcase()
    return str


HOST = ''
PORT = 300
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print('Listening to {}'.format(server_socket.getsockname()))

try:
    while True:
        client, address = server_socket.accept()
        data = client.recv(BUFFER_SIZE)

        if data:
            msg = data.decode('ascii')
            print('Client''s address {}'.format(address))
            rev_msg = reversed_string(msg)
            data = rev_msg.encode('ascii')
            client.send(data)
finally:
    client.close()
