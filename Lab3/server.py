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



#class that manages the planet list, it also contains a method for calculating a new position for a planet given all the other.
#DT is the delta-time that specify the increment in time for planet updates. No need to change this.
############## NOTE!!!!! THIS CLASS IS NOT THREAD SAFE AND NEEDS TO BE PROTECTED USING SOME FORM OF MUTEXES
class universe:
    '''
    Class that manages the list of planets in the universe. In the lab you will need to extend this class with your own methods to manage the planets.
    '''


    planet_list=[]  #The actual list
    DT : int        

    
    def __init__(self, dt=10):
        '''Constructs a universe (i.e. a list of planets), delta time is set to 10 by default which you probably dont need to change. '''
        self.planet_list.clear()
        self.DT=dt

    def calculate_planet_pos(self,p:planet):
        '''Method to  calculate the position of planet p, relative to all other planets in the system. The method updates the position and age of planet p''' 
        Atotx = 0.0
        Atoty = 0.0
        x = 0.0
        y = 0.0
        r = 0.0
        a = 0.0
        ax = 0.0
        ay = 0.0
        
        G = 6.67259 * pow(10, -11) #Declaration of the gravitational constant
        
        cur:planet
        for cur in self.planet_list:
            if (cur!=p):
                x = cur.sx-p.sx
                y=cur.sy-p.sy
                r = sqrt(pow(x, 2) + pow(y, 2))
                a = G * (cur.mass / pow(r, 2))

                ay = a * (y / r)
                ax = a * (x / r)

                Atotx += ax
                Atoty += ay
    
        p.vx = p.vx + (Atotx * self.DT) #Update planet velocity, acceleration and life
        p.vy = p.vy + (Atoty * self.DT)
        p.sx = p.sx + (p.vx * self.DT)
        p.sy = p.sy + (p.vy * self.DT)
        p.life -= 1
    
    # Here you need to extend the planets class with your own methods to manage the planets


def randpaint(s:space):
    '''A demonstration function for the lab-package. Prints a randomly moving planet on the canvas. Just demonstrates how to draw, should be removed when lab is implemented.'''
    x=SPACEX/2
    y=SPACEY/2
    random.seed()
    while(True):
        x=x+random.randint(-3,3)
        if(x<0): x=0
        if(x>SPACEX-1): x=SPACEX-1
        y=y+random.randint(-3,3)
        if(y<0): y=0
        if(y>SPACEY-1): y=SPACEY-1
        s.putPlanet(x,y,rad=2,color="red")
        time.sleep(0.01)



def main():
    # Create the universe (i.e, an empty set of planets)
    u=universe()  
    # Create the window on which to draw the universe
    s=space(SPACEX,SPACEY)

    # USER CODE GOES HERE....

    painter=threading.Thread(target=randpaint, args=(s,), daemon=True)
    painter.start()

    # Last part of main function is the window management loop, will terminate when window is closed
    s.mainLoop()

if __name__== "__main__":
    main()

