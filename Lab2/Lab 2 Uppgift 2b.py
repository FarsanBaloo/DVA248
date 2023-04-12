import time
import threading
import sys


def Philosopher(i, gafflar):
    print("Philosopher", i+1, "\n")
    while True:
        time.sleep(0.1)  # Thinking

        while gafflar._value == 1:
            time.sleep(1)
            # print("-------------------------waiting------------------------")
        gafflar.acquire()         # Gaffel 1
        gafflar.acquire()         # Gaffel 2

        for letter in "eating":
            time.sleep(0.5)

        print("Philosopher", i+1, "is full. \n")
        gafflar.release()
        gafflar.release()

        print("Philsopher", i+1, "has put back their forks. \n")


def phi(numPhi, sema):
    for prod in range(numPhi):
        # Create the producer threads
        threading.Thread(target=Philosopher, args=(prod, sema), daemon=True).start()
        # Add code to start numProd producer() thread(s)
    sys.exit()

def main():
    numPhi = 5
    sema = threading.Semaphore(5)  # Gafflar?
    threading.Thread(target=phi, args=(numPhi, sema), daemon=True).start()

    time.sleep(60)


if __name__ == "__main__":
    main()