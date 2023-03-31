import time
from planet import planet
from cscomm import clientInitSocket,clientRecvString,clientSendPlanet

p=planet("Sun",300,300,0,0,10e8,10e8)

s=clientInitSocket()           
clientSendPlanet(s,p)
s.close()   

