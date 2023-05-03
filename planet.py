#Module for planet class for DVA248 Datorsystem
#
#   author: Dag Nyström, 2023
#

import socket

class planet:
    '''
    Class that contains planet objects.
    The class is shared between server and client,
    however the methods are only used in the server.
    
    '''
    name:str
    sx:float
    sy:float
    vx:float
    vy:float
    mass:float
    life:int
    cSock:socket #ONLY USED BY SERVER

    def __init__(self,name, sx, sy,vx,vy,mass,life,color,radius):
        self.name=name
        self.sx=sx
        self.sy=sy
        self.vx=vx
        self.vy=vy
        self.mass=mass
        self.life=life
        self.cSock=None
        self.color=color
        self.radius=radius


    #ONLY USED BY SERVER, do not send socket from client to server.
    def serverAddClientSock(self,cSock):
        '''
        Server-side method to add the socket of the corresponding client to the planet object.
            cSock:  The client socket to add to the planet
        '''
        self.cSock=cSock

    #ONLY USED BY SERVER, do not send socket from client to server.
    def serverGetClientSock(self):
        '''
        Server-side method to retrieve the associated client socket from a planet object.
        The method returns the socket.
        '''
        return self.cSock