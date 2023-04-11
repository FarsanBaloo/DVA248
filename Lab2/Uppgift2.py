import time
import threading


def Philosopher(i, gafflar):
    print("Philosopher", i)
    while True:
        time.sleep(0.1)  # Thinking

        gafflar[i].acquire()         # Gaffel 1
        gafflar[(i+1)%5].acquire()   # Gaffel 2
        # Pickup fork i and fork (i+1)%5
        for letter in "eating":
            time.sleep(0.5)
            # print(letter, end="")
        print()
        print("Philosopher", i, "is full.")
        gafflar[i].release()
        gafflar[(i+1)%5].release()
        print("Philsoopher", i, "has put back their forks.")

        # Print(Filosof i har nu plockat upp sina gafflar)
        # Eat
        # Print(Filosof i är nu mätt)
        # Place fork i and fork (i+1)%5
        # Print(Filosof i har nu lagt tillbaks sina gafflar)hilosopher(i):


def phi(numPhi, sema):
    for prod in range(numPhi):
            # Create the producer threads
            threading.Thread(target=Philosopher, args=(prod, sema), daemon=True).start()
            # Add code to start numProd producer() thread(s)

def main():
    numPhi = 5
    sema = threading.Semaphore(5)  # Gafflar?
    # Lock_1 = threading.Lock()
    # Lock_2 = threading.Lock()
    # Lock_3 = threading.Lock()
    # Lock_4 = threading.Lock()
    # Lock_5 = threading.Lock()
    # Locks = [Lock_1, Lock_2, Lock_3, Lock_4, Lock_5]   # Vafan gafflar du om??
    t1 = threading.Thread(target=phi, args=(numPhi, sema), daemon=True)
    # t1 = threading.Thread(target=Philosopher, args=(0, sema), daemon=True)
    # t2 = threading.Thread(target=Philosopher, args=(1, sema), daemon=True)
    # t3 = threading.Thread(target=Philosopher, args=(2, sema), daemon=True)
    # t4 = threading.Thread(target=Philosopher, args=(3, sema), daemon=True)
    # t5 = threading.Thread(target=Philosopher, args=(4, sema), daemon=True)
    t1.start()
    #Philosopher(sema)

    time.sleep(30)



if __name__ == "__main__":
    main()