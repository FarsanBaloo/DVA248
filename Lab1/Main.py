import time
import threading


def myMoon():
    while True:
        print("Hello Moon!")
        time.sleep(0.2)


def main():
    myMoon()
    i = 0
    while i < 10:
        print("Hello World", i)
        time.sleep(0.5)
        i += 1


if __name__ == '__main__':
    main()

