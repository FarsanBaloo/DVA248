import time
import threading as thread


def myMoon(argument):
    while True:
        print(argument)
        time.sleep(0.2)


def main():
    argument = input('Skriv lite text: ')
    t1 = thread.Thread(target=myMoon, args=(argument,), daemon=True)
    t1.start()
    i = 0
    while i < 10:
        print("Hello World", i)
        time.sleep(1)
        i += 1


if __name__ == '__main__':
    main()
