import time
import threading


def myMoon(argument, lock):
    while True:
        lock.acquire()
        i = 0
        while i < 10:
            print(argument)
            time.sleep(0.2)
            i += 1
        lock.release()
        time.sleep(0.1)


def main():
    argument = input('Skriv lite text: ')
    lock = threading.Lock()
    t1 = threading.Thread(target=myMoon, args=(argument, lock), daemon=True)
    t1.start()
    while True:
        lock.acquire()
        i = 0
        while i < 10:
            print("Hello World", i)
            time.sleep(0.5)
            i += 1
        lock.release()
        time.sleep(0.1)


if __name__ == '__main__':
    main()