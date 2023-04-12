import time
import threading


def Philosopher(i, gafflar):
    while True:
        print(f"Philosoph {i + 1} tänker. \n")
        time.sleep(0.1)  # Philosoph tänker

        """Jämn placering av philosph tar vänster först sedan höger & släpp vänster gaffel om inte får höger gaffel"""
        if i % 2 == 0:
            gafflar[i].acquire()                                # Tar Vänster gaffel
            if not gafflar[(i + 1) % 5].acquire(timeout=1):     # Försök ta höger gaffel annars släpp vänster gaffel
                print(f"Philosoph {i + 1} har inte fått höger gaffel så släpper den vänstra gaffeln.\n")
                gafflar[i].release()                            # Släpp vänster gaffel

        """Udda placering av philosph tar höger först sedan vänster & släpper höger gaffel om inte får vänster gaffel"""

        if i % 2 == 1:
            gafflar[(i + 1) % 5].acquire()                      # Ta höger gaffel
            if not gafflar[i].acquire(timeout=1):               # Försök att ta vänster gaffel annars släpp höger gaffel
                print(f"Philosoph {i + 1} har inte fått vänster gaffel så släpper den högra gaffeln.\n")
                gafflar[i + 1].release()                        # Släpp höger gaffel

        print(f"Philosoph {i + 1} börjar Ätta. \n")
        time.sleep(3)  # ätter

        # Ättit klart Lägger ner båda gafflarna
        gafflar[i].release()
        gafflar[(i+1) % 5].release()
        print(f"Philsoph {i+1} har ättit klart & har lagt ner gafflarna!.")


def phi(numPhi,gafflar):
    for prod in range(numPhi):
        threading.Thread(target=Philosopher, args=(prod, gafflar), daemon=True).start()


def main():
    numPhi = 5
    gaffel1 = threading.Semaphore()
    gaffel2 = threading.Semaphore()
    gaffel3 = threading.Semaphore()
    gaffel4 = threading.Semaphore()
    gaffel5 = threading.Semaphore()
    gafflar = [gaffel1, gaffel2, gaffel3, gaffel4, gaffel5]

    t1 = threading.Thread(target=phi, args=(numPhi, gafflar), daemon=True)
    t1.start()

    time.sleep(60)


if __name__ == "__main__":
    main()