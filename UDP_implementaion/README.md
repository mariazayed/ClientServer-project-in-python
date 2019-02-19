## UDP Protocol
UDP or User Datagram Protocol is connection-less protocol which is suitable for applications that require efficient communication that doesn't have to worry about packet loss.

### Client implementation steps :
1. #### Import the socket library
2. #### Declare variables for specifying the IP address `HOST`, port number `PORT` that the message will be send through, and the size of the message `BUFFER_SIZE`<br>
    ```
    HOST = '192.168.1.112'
    PORT = 300
    BUFFER_SIZE = 1024
    ```
    **NOTE:** the IP address is __my machine address__, it obtains from `ipconfig` command (for Windows) or `ifconfig` (for Linux and MacOS)
    
    ![1](https://user-images.githubusercontent.com/27064594/53001224-d058cb00-3432-11e9-8263-9b6f79e78911.PNG)
3. #### Socket Creation:<br>
    ```client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)```<br>
    in socket creation it is important to define two things **address family**, and **connection type**
      - **AF_INET**: is an address family that is used to designate the type of addresses that the socket can communicate with (in this case, Internet Protocol v4 addresses)
      - **SOCK_DGRAM**: is the type of communications between the two endpoints, _SOCK_DGRAM_ for connectionless protocols (UDP)
4. #### Send a Message:<br>
    ```client_socket.sendto(data, (HOST, PORT))```
    - For sending a message in UDP protocol is it enough to know the IP and port number for the receiver 
    - Note that _data_ is encoded version of the client’s message. This done for security issues
5. #### Set Time Out and receive the response message:<br>
    In UDP, when a client send a message, he doesn’t have any information about the state of network or about the server. In this case the sending packets will be drop if there is any problem in the network or the server. For this reason, ```settimeout``` function from socket library was used.<br>
    Here the client will wait for a half minute before receiving a response message. If not, an error message will be shown .<br>
    ```
        client_socket.settimeout(delay)
    
        try:
            data, server_address = client_socket.recvfrom(BUFFER_SIZE)
        except socket.timeout as exc:
            delay += 0.1
            if delay > 0.5:
                raise RuntimeError('SERVER IS DOWN !') from exc
        else:
                break
    ```
6. #### Close the Socket:<br>
    ```client_socket.close()``` This line closes the socket and terminates the proces.
    
    
    
    
 ### Server implementation steps :
 #### Steps 1,2, and 3 same as UDP client implementation.<br>
4. #### Bind the Socket:<br>
    ```server_socket.bind((HOST, PORT))``` This method binds address _(hostname, port number)_ pair to socket.<br>
      In this step, the server is listening on our defined IP address and port number for any UDP messages.<br>
      To be sure that the bind function works properly, a simple print statement was used:<br>
    ```print('Listening to {}'.format(server_socket.getsockname()))```
      - getsockname() function returns the client’s IP and port numbers

5. #### Receive a message:<br>
    To keep the server continuously listening to the client until the socket termination, a while loop was used:
      ```
        while True:
            data, client_address = server_socket.recvfrom(BUFFER_SIZE)
      ``` 
      Any server is receiving a messages from many clients. To know the IP of these client’s, a simple print statement was used: 
      ```print('Client''s address {}'.format(client_address))```<br>
      **Note** that the client and server don’t use the same port number. For example, server is listening on port 80, when client connect to server, it will connect to server IP address on port 80. But client socket is live on another port, it is allocated by OS
6. #### Accomplish the response message:<br>
      - **Reverse all the characters:**<br>
        This could be done by a simple function in python3:<br>
        ```str = string[::-1]```<br>
        This function takes three parameters ```[start:end:step]``` in this case, the function takes the string and extracts the characters according to the *step* variable (-1, in this case), which reversed the string.<br>
        **Note** that this function also works for tuples and arrays
      - **Reverse the capitalization of the string:**<br>
        This is done by a ```swapcase()``` function in python. This method returns a copy of the string in which all the case-based characters have had their case swapped.
7. #### Send the response message:<br>
In this step, the response message is ready to send. The server sends the response message to the *address* variable that received from ```recvfrom()``` function.
