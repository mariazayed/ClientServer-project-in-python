import socket

HOST = '192.168.1.112'
PORT = 300
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

delay = 0.1
message = input("Input message:")
data = message.encode('ascii')

client_socket.sendto(data, (HOST, PORT))

print('waiting {} seconds for reply'.format(delay))
client_socket.settimeout(delay)

try:
    data, server_address = client_socket.recvfrom(BUFFER_SIZE)
except socket.timeout as exc:
    delay += 0.1
    if delay > 0.5:
        raise RuntimeError('SERVER IS DOWN !') from exc

print('The SERVER replies : {}'.format(data.decode('ascii')))
client_socket.close()
