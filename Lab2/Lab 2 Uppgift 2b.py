import time
import threading
import sys


def Philosopher(i, gafflar):
    print("Philosopher", i+1, "\n")
    while True:
        time.sleep(0.2)  # Thinking
        while gafflar._value == 1:
            time.sleep(1)
            print("-------------------------waiting------------------------")
        gafflar.acquire()         # Gaffel 1
        # print(f"Acquire 1: ", gafflar._value, "held by philosopher", i+1, "\n")
        gafflar.acquire()         # Gaffel 2
        # print(f"Acquire 2: ", gafflar._value, "held by philosopher", i+1, "\n")
        # gafflarkvar= gafflar._value
        # for letter in "eating":
        #     time.sleep(0.5)
        # print()
        print("Philosopher", i+1, "is full. \n")
        gafflar.release()
        # print(f"Release 1: ", gafflar._value, "held by philosopher", i+1, "\n")
        gafflar.release()
        # print(f"Release 2: ", gafflar._value, "held by philosopher", i+1, "\n")
        print("Philsopher", i+1, "has put back their forks. \n")


def phi(numPhi, sema):
    for prod in range(numPhi):
        # Create the producer threads
        threading.Thread(target=Philosopher, args=(prod, sema), daemon=True).start()
        # Add code to start numProd producer() thread(s)

def main():
    numPhi = 6
    sema = threading.Semaphore(5)  # Gafflar?
    threading.Thread(target=phi, args=(numPhi, sema), daemon=True).start()

    time.sleep(60)


if __name__ == "__main__":
    main()