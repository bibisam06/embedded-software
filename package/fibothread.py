from threading import Thread, Lock
import sys


total = 0
a, b = 0, 0
def addsum(n, lock):

    for i in range(n):
        global total
        global a , b
        with lock:
            total = a+b
            print(total)
            a, b = b, a+b



lock = Lock()

n1 = int(sys.argv[1])

t1 = Thread(target=addsum, args = (0, 1, n1, lock))
t2 = Thread(target=addsum, args = (a, b, lock))
t1.start()
t2.start()


