#Planet lab in Python for DVA248 Datorsystem
#
#   author: Dag Nyström, 2020
#

import threading
import random 
import time
import socket
from space import space
from cscomm import serverInitSocket,serverWaitForNewClient,serverRecvPlanet,serverSendString
from planet import planet
from math import sqrt


SPACEX=800
'''Constant for width of the universe in pixels/coordinates'''
SPACEY=600
'''Constant for height of the universe in pixels/coordinates'''


# Class that manages the planet list, it also contains a method for calculating a new position for a planet given all the other.
# DT is the delta-time that specify the increment in time for planet updates. No need to change this.
# ############# NOTE!!!!! THIS CLASS IS NOT THREAD SAFE AND NEEDS TO BE PROTECTED USING SOME FORM OF MUTEXES
class universe:
    '''
    Class that manages the list of planets in the universe. In the lab you will need to extend this class with your own methods to manage the planets.
    '''


    planet_list=[]  #The actual list
    DT : int        

    
    def __init__(self, dt=10):
        '''Constructs a universe (i.e. a list of planets),
        delta time is set to 10 by default which you probably dont need to change. '''
        self.planet_list.clear()
        self.DT=dt

    def calculate_planet_pos(self,p:planet,s, handcuffs):
        '''
        Method to  calculate the position of planet p, relative to all other planets in the system.
        The method updates the position and age of planet p
        '''
        Atotx = 0.0
        Atoty = 0.0
        x = 0.0
        y = 0.0
        r = 0.0
        a = 0.0
        ax = 0.0
        ay = 0.0
        
        G = 6.67259 * pow(10, -11) # Declaration of the gravitational constant

        cur:planet
        for i, cur in enumerate(self.planet_list):
            if (cur!=p):
                handcuffs.acquire()
                x = cur.sx-p.sx
                y=cur.sy-p.sy
                r = sqrt(pow(x, 2) + pow(y, 2))
                a = G * (cur.mass / pow(r, 2))
                ay = a * (y / r)
                ax = a * (x / r)
                Atotx += ax
                Atoty += ay
                handcuffs.release()
                if cur.life == 0:
                    print(cur.name, "is old! Doom befalls us all!")
                    self.planet_list.pop(i)
                if self.isOutofBonds(cur):
                    print(cur.name, "is gone! Doom befalls us all!")
                    self.planet_list.pop(i)

        handcuffs.acquire()
        p.vx = p.vx + (Atotx * self.DT) # Update planet velocity, acceleration and life
        p.vy = p.vy + (Atoty * self.DT)
        p.sx = p.sx + (p.vx * self.DT)
        p.sy = p.sy + (p.vy * self.DT)
        handcuffs.release()
        s.putPlanet(p.sx, p.sy, rad=p.radius, color=p.color)
        p.life -= 1

    def isOutofBonds(self, p):
        if p.sx > SPACEX or p.sx < 0:
            return True
        if p.sy > SPACEY or p.sy < 0:
            return True
        return False

    
    # Here you need to extend the planets class with your own methods to manage the planets


def newPlanet(clientSocket, u, p, s, handcuffs):
    u.planet_list.append(p)
    while p in u.planet_list:
        universe.calculate_planet_pos(u, p, s, handcuffs)
        time.sleep(0.01)
    if p.life <= 0:
        serverSendString(clientSocket, f"{p.name} grew too old and imploded!! Doom befalls us all!")
    if universe.isOutofBonds(u, p):
        serverSendString(clientSocket, f"{p.name} escaped the known universe!! Coward! ")


def clientThread(clientSocket, u, s, handcuffs):
    p = serverRecvPlanet(clientSocket)
    serverSendString(clientSocket, f"{p.name} recieved! Thanks for your patronage")
    # print(f"The big planet is: {p.name, p.sx, p.sy,p.vx, p.vy, p.mass, p.life}")
    threading.Thread(target=newPlanet, args=(clientSocket, u, p, s, handcuffs), daemon=True).start()


def serverThread(serverSocket, u, s, handcuffs):

    while True:
        clientSocket = serverWaitForNewClient(serverSocket)
        threading.Thread(target=clientThread, args=(clientSocket, u, s, handcuffs), daemon=True).start()
        time.sleep(0.1)


def main():
    # Create the universe (i.e, an empty set of planets)
    u=universe()  
    # Create the window on which to draw the universe
    s=space(SPACEX,SPACEY)

    # USER CODE GOES HERE....
    handcuffs = threading.Lock()
    serverSocket = serverInitSocket()
    threading.Thread(target=serverThread, args=(serverSocket, u, s, handcuffs), daemon=True).start()

    # Last part of main function is the window management loop, will terminate when window is closed
    s.mainLoop()


if __name__ == "__main__":
    main()

