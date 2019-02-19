## TCP Protocol
The TCP or Transmission Control Protocol is a connection-oriented protocol. It determines how to break application data into packets that networks can deliver, sends packets to and accepts packets from the network layer, manages flow control, and retransmission of dropped or garbled packets as well as acknowledgment of all packets that arrive.  

### Client Implementation steps:
1. #### Import the socket library
2. #### Declare variables for specifying the IP address ```HOST```, port number ```PORT```  that the message will be sent through, and the size of the message ```BUFFER_SIZE```
    ```
    HOST = 'localhost'
    PORT = 300
    BUFFER_SIZE = 1024
    ```
    -	**Note** that, it is allowed for ```HOST``` to take a value of ```localhost``` or ```‘’``` (empty quotations) instead of IP address, python will automatically knows that the IP of the working machine is the intent
3. #### Socket Creation:
    ```client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)```<br>
    in socket creation it is important to define two things address **family**, and **connection type**
      -	**AF_INET**: is an address family that is used to designate the type of addresses that the socket can communicate with (in this case, Internet Protocol v4 addresses)
      -	**SOCK_STREAM**: is the type of communications between the two endpoints, SOCK_STREAM for connection-oriented protocols (TCP)
4. #### Handshaking:
    This is done by ```conenect()``` function:<br>
      ```client_socket.connect((HOST, PORT))```<br>
    This method actively initiates TCP server connection.
5. #### Send a Message:
    ```client_socket.send(message.encode('ascii'))```
      -	**Send()** function is used to transmit a message in TCP connection, because of the handshaking in TCP, in this function there is no need to mention the receiver’s address. But ```sendto()``` function is used in UDP connection, and because of there is no handshaking in UDP, it is necessary to mention the receiver’s address
6. #### Receive the response message:
    ```data = client_socket.recv(BUFFER_SIZE)```
      -	**Recv()** function is used to receive a message in TCP connection, there is no way to know the sender’s IP using this function, and there is no need to know the Sender’s IP when the TCP connection in running, this function returns the response message only. But ```recvfrom()```  function is used in UDP connection, this function returns the sender’s IP address plus the response message.
7. #### Close the socket:<br>
    ```client_socket.close()``` 
    This line closes the socket and terminates the process
    
![c](https://user-images.githubusercontent.com/27064594/53013428-7960ef00-344e-11e9-8ab7-71622099fa05.PNG)



### Server implementation steps:
#### Steps 1,2, and 3 same as TCP client implementation.
4.	#### Bind the Socket and start listening :
    ```
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
    ```
    - **bind()** method binds address *(hostname, port number)* pair to socket.<br>
    - **Listen()** method sets up and start TCP listener.<br>
  In this step, the server is listening on our defined IP address and port number for any TCP messages. To be sure that the bind and       listen functions are work properly, a simple print statement was used:<br>
    ```print('Listening to {}'.format(server_socket.getsockname()))```
     - **getsockname()** function returns the client’s IP and port numbers
    
5.	#### Receive a message:
    To keep the server continuously listening to the client until the socket termination, a while loop was used.<br>
    ```
     while True:
         client, address = server_socket.accept()
          data = client.recv(BUFFER_SIZE)
     ```
    - **accept()** function returns an open connection between the server and client, along with the address of the client. 
            The connection is actually a different socket on another port 
    - Data is read from the connection with **recv()**
    
6.	#### Accomplish the response message:
    **Same functionality as server implementation in UDP**<br>

7.	#### Send the response message:
    In this step, the response message is ready to send. The server sends the response message to the client using **send()** function. 

8.	#### Close the connection:
    When communication with a client is finished, the connection needs to be cleaned up using **close()** function. To ensure that           close() is always called, even in the event of an error, a ```try-finally``` block is used

![d](https://user-images.githubusercontent.com/27064594/53013452-84b41a80-344e-11e9-9b07-779d6788f35c.PNG)
