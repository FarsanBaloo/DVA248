import time
import threading
from planet import planet
from cscomm import clientInitSocket,clientRecvString,clientSendPlanet

# def send(s, p):
#     clientSendPlanet(s,p)
#
# def starbody(name, x, y, z, b, n, m):
#     yield planet(name, x, y, z, b, n, m)
p=planet("Sun",300,300,0,0,10e8,10e8,"orange")

#thep=planet("moon",3,3,0,0,3,3)
# for p in starbody("Sun", 300, 300, 0, 0, 10e8, 10e8):
#     threading.Thread(target=send, args=(s,p), daemon=True).start()

s=clientInitSocket()           
clientSendPlanet(s,p)
# clientSendPlanet(s,thep)
message = clientRecvString(s)
print(message)
s.close()   

