import time
import threading


def Philosopher(i, gafflar):
    while True:
        print("\nPhilosoph ", i + 1, " Tänker.")
        time.sleep(1)  # Thinking

        # Förhindra backlås där alla filosofers tar en vänster gaffel samtidigt

        # Jämn placering av philosph tar vänster gaffel först sedan höger
        if i % 2 == 0:
            gafflar[i].acquire()                    # Vänster gaffel
            gafflar[(i + 1) % 5].acquire()          # Höger gaffel

        # Udda placering av philosph tar höger gaffel först sedan vänster
        if i % 2 == 1:
            gafflar[(i + 1) % 5].acquire()          # Höger gaffel
            gafflar[i].acquire()                    # Vänster gaffel

        print("\nPhilosoph ", i + 1, " Börjar Ätta.")
        time.sleep(1)  # ätter

        # Ättit klart Lägger ner båda gafflarna
        gafflar[i].release()
        gafflar[(i+1) % 5].release()
        print("\nPhilsoph ", i+1, " Har ättit klart och läggat ner gafflarna.")


def phi(numPhi,gafflar):
    for prod in range(numPhi):
        threading.Thread(target=Philosopher, args=(prod, gafflar), daemon=True).start()


def main():
    numPhi = 5
    gaffel1 = threading.Semaphore(1)
    gaffel2 = threading.Semaphore(1)
    gaffel3 = threading.Semaphore(1)
    gaffel4 = threading.Semaphore(1)
    gaffel5 = threading.Semaphore(1)
    gafflar = [gaffel1, gaffel2, gaffel3, gaffel4, gaffel5]

    t1 = threading.Thread(target=phi, args=(numPhi, gafflar), daemon=True)
    t1.start()

    time.sleep(60)


if __name__ == "__main__":
    main()