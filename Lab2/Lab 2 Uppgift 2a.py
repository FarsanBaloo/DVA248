import time
import threading


def Philosopher(i, gafflar, Used):
    print("Philosopher", i)
    while True:
        time.sleep(0.1)  # Thinking

        while Used[i] and Used[(i+1)%5]:
            time.sleep(1)
            print("------waiting-------"*5)

        gafflar[i].acquire()
        Used[i] = True

        gafflar[(i+1)%5].acquire()
        Used[(i+1)%5] = True

        for letter in "eating":
            time.sleep(0.5)
        print()
        print("Philosopher", i, "is full.")

        gafflar[i].release()
        Used[i] = False

        gafflar[(i+1)%5].release()
        Used[(i + 1) % 5] = False

        print("Philsoopher", i, "has put back their forks.")


def main():
    numPhi = 5
    Lock_1 = threading.Lock()
    Lock_2 = threading.Lock()
    Lock_3 = threading.Lock()
    Lock_4 = threading.Lock()
    Lock_5 = threading.Lock()
    Locks = [Lock_1, Lock_2, Lock_3, Lock_4, Lock_5]   # Vafan gafflar du om??
    Used = [False]*5
    t1 = threading.Thread(target=Philosopher, args=(0, Locks, Used), daemon=True)
    t2 = threading.Thread(target=Philosopher, args=(1, Locks, Used), daemon=True)
    t3 = threading.Thread(target=Philosopher, args=(2, Locks, Used), daemon=True)
    t4 = threading.Thread(target=Philosopher, args=(3, Locks, Used), daemon=True)
    t5 = threading.Thread(target=Philosopher, args=(4, Locks, Used), daemon=True)
    t1.start(), t2.start(), t3.start(), t4.start(), t5.start()

    time.sleep(30)


if __name__ == "__main__":
    main()