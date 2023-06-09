import threading
import time

# the buffer and its global index
buffer = [None,None,None,None,None]
bufferIndex=0

# The individual number of the item
productItemNo=0


# Producer Thread 
def producer(no:int, prod_sema, cons_sema, Lock):
    global productItemNo
    item=0
    print("Producer "+str(no)+" created!")
    while(True):
        # sleep for a little bit of time 
        time.sleep(0.1)

        # Obtain a number of the new item to produce
        item = productItemNo
        productItemNo+=1

        # Produce the item to the buffer
        prod_sema.acquire()
        ret=insert_item(item, Lock)
        cons_sema.release()

        if(ret):
            print("producer "+str(no)+" produced "+str(item)+"\n")
            
        else:
            print(" Producer "+str(no)+" report error - full buffer\n") 
        

# Consumer Thread 
def consumer(no:int, prod_sema, cons_sema, Lock):
    item = 0
    print("Consumer "+str(no)+" created!")
    while True:
        # sleep for little bit of time 
        time.sleep(0.1)
        # Consume one item from the buffer, ret (True False), item (itemnumber)

        cons_sema.acquire()
        ret, item = remove_item(Lock)
        prod_sema.release()
        if(ret):
            print("consumer "+str(no)+" consumed " + str(item)+"\n") 
        else:
            print("Consumer "+str(no)+" report error condition - buffer empty\n")


# Add an item to the buffer 
def insert_item(item:int, Lock):
    global bufferIndex
    #When the buffer is not full add the item
    # and increment the bufferIndex
    with Lock:
        if bufferIndex < 5:
            buffer[bufferIndex] = item
            bufferIndex+=1
            return True

        else: # Error the buffer is full
            return False


# Remove an item from the buffer */
def remove_item(Lock):
    global bufferIndex
    # When the buffer is not empty remove the item
    # and decrement the bufferIndex
    with Lock:
        if bufferIndex > 0:
            item = buffer[(bufferIndex-1)]
            bufferIndex -= 1
            return True,item

        else: # Error buffer empty
            return False,None


def thread_prod(numProd, prod_sema, cons_sema, Lock):
    for prod in range(numProd):
        # Create the producer threads
        threading.Thread(target=producer, args=(prod, prod_sema, cons_sema, Lock), daemon=True).start()
        # Add code to start numProd producer() thread(s)


def thread_cons(numCons, prod_sema, cons_sema, Lock):
    """  Create the consumer threads  """
    for cons in range(numCons):
        threading.Thread(target=consumer, args=(cons, prod_sema, cons_sema, Lock), daemon=True).start()


def main():
    # THESE SHOULD BE CHANGED ACCORDING TO THE LAB SPECIFICATION   
    numProd = 10    # Number of producer threads
    numCons = 300   # Number of consumer threads

    # lock = threading.Lock()
    prod_sema = threading.Semaphore(5)
    cons_sema = threading.Semaphore(0)
    Lock = threading.Lock()
    t1 = threading.Thread(target=thread_prod, args=(numProd, prod_sema, cons_sema, Lock), daemon=True)
    t2 = threading.Thread(target=thread_cons, args=(numCons, prod_sema, cons_sema, Lock), daemon=True)
    t1.start(), t2.start()

    # Let the program run for 10 seconds
    time.sleep(10)


if __name__== "__main__":
    main()