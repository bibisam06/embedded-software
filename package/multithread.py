from threading import Thread, Lock
import sys

total = 0
def add(n, lock):
    global total
    with lock:
        total += n

if __name__ =='__main__':
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])

    lock = Lock()
    t1 = Thread(target=add, args = (n1, lock))
    t2 = Thread(target=add, args = (n2, lock))

    t1.start()
    t2.start()
    print('sum='+str(total))
