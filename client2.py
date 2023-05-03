import time
import threading
from planet import planet
from cscomm import clientInitSocket,clientRecvString,clientSendPlanet

# planet(Name, X-pos, Y-pos, X-velocity, Y-Velocity, Mass, Life, color, radius)
planets = [planet("Oops",500,400,0,0,10e9,100,"red", radius=10)]

def sendPlanets(p):
    s = clientInitSocket()
    clientSendPlanet(s,p)
    for i in range(2):
        message = clientRecvString(s)
        print("\n", message, "\n")
    s.close


while planets:
    p = planets.pop()
    threading.Thread(target=sendPlanets, args=(p,), daemon=True).start()
    time.sleep(0.1)
while True:
    print()
    name = input("Planet Name > ")
    if name.lower() == "exit" or "":
        exit()
    try:
        X = int(input("X-Pos > "))
        Y = int(input("Y-Pos > "))
        X_vel = float(input("X Velocity > "))
        Y_vel = float(input("Y Velocity > "))
        mass = int(input("Mass > "))
        life = int(input("Life(ticks) > "))
        color = input("Color > ")
        radius = int(input("Radius > "))
    except ValueError:
        print("Try with numbers.")
        continue
    p = planet(name, X, Y, X_vel/1000, Y_vel/1000, mass, life, color, radius)
    threading.Thread(target=sendPlanets, args=(p,), daemon=True).start()
