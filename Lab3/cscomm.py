#Module for socket communication for DVA248 Datorsystem
#
#   author: Dag Nystrom, 2023
#
import socket
import pickle

##########################
#### SERVER-SIDE FUNCTIONS
##########################

def serverInitSocket (ip='127.0.0.1',port=12345):
    '''
    Server-side function to create a socket for new client connections.
        ip:     a string containing the IP address to the server, default is localhost.
        port:   an int containing the port to listen to, default is 12345
    Returns a socket object
    '''
    serverSocket: socket
    #<Implementation here>
    HOST, PORT = ip, port
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ???????????????????
    serverSocket.bind((HOST, PORT))

    # print("Hej!")
    # try:
    #     while True:
    #         conn, addr = soc.accept()
    #         request = conn.recv(1024).decode()
    #         # print(request)

    return serverSocket 

def serverWaitForNewClient(serverSocket:socket):
    '''
    Server-side function that makes the server wait for a new client connecting on the server socket.
        serverSocket:   the socket used for new client connections
    Returns a socket to the new client
    '''
    clientSocket:socket
    # Note: All clients can be accepted for this lab since only local communication is allowed.
    #<Implementation here>
    serverSocket.listen()
    clientSocket, adress = serverSocket.accept()

    return clientSocket

def serverSendString(clientSocket:socket, mess:str):
    '''
    Server-side function to transmit a string from the server to the client via the client socket
        clientSocket:   the socket to transmit on
        mess:           the message to transmit
    '''
#   Note: Function must transform UNICODE strings to byte strings
    # <Implementation here>
    clientSocket.send(pickle.dumps(mess))
    return

def serverRecvPlanet(clientSocket:socket):
    '''
    Server-side function to receive a planet object from a client over the client socket.
    The function waits until it receives a planet.
        clientSocket:   the socket to receive from
    Returns the planet object
    '''
    # Note: Function must recreate object from bytestring
    # <Implementation here>

    small_P = clientSocket.recv(4096)
    bigP = pickle.loads(small_P)
    return bigP

#########################
### CLIENT-SIDE FUNCTIONS
#########################


def clientInitSocket (ip='127.0.0.1',port=12345):
    '''
    Client-side function to connect to a server via its connecting socket
        ip:     a string containing the IP address to the server, default is localhost
        port:   and integer with the portnumber to use, default is 12345
    Returns a client socket to communicate with the server over
    '''
    clientSocket:socket
    # <Implementation here>
    HOST, PORT = ip, port
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ???????????????????
    clientSocket.connect((HOST, PORT))
    
    return clientSocket


def clientRecvString(clientSocket:socket):
    '''
    Client-side function to receive a string from the server over a socket
        clientSocket:   the socket used for communication with the server
    Returns the string.
    '''
    message:str
    #<Implementation here>

    message = pickle.loads(clientSocket.recv())

    # small_P = clientSocket.recv()
    # bigP = pickle.loads(small_P)
    
    return message


def clientSendPlanet(clientSocket:socket, p:object):
    '''
    Client-side function to send a planet object to the server over a socket
        clientSocket:   the socket used for communication with the server
        p:              the planet object to transmit'''
#   Note: Function must transform object into bytestring
    #<Implementation here>

    clientSocket.send(pickle.dumps(p))
    # bigP = pickle.loads(small_P)

    return

    
    