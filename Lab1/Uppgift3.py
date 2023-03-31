import time
import threading


def myMoon(argument, lock):
    lock.acquire()
    i = 0
    while i < 10:
        print(argument)
        time.sleep(0.2)
        i += 1
    lock.release()


def main():
    argument = input('Skriv lite text: ')
    lock = threading.Lock()
    t1 = threading.Thread(target=myMoon, args=(argument, lock), daemon=True)
    t1.start()
    lock.acquire()
    i = 0
    while i < 10:
        print("Hello World", i)
        time.sleep(0.5)
        i += 1
    lock.release()


if __name__ == '__main__':
    main()
