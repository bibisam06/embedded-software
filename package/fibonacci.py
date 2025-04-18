from threading import Thread, Lock, Condition
import sys


class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0
        self.turn = 0
        self.lock = Lock()
        self.condition = Condition(self.lock)

    def addsun(self, thread_id):
        while True:
            with self.condition:
                if self.count >= self.n:
                    return
                if self.turn != thread_id:
                    self.condition.wait()
                else:
                    print(self.a)
                    self.a, self.b = self.b, self.a + self.b
                    self.count += 1
                    self.turn = 1 - thread_id
                    self.condition.notify_all()

if __name__ == "__main__":

    fib = Fibonacci(10)

    t1 = Thread(target=fib.addsun, args = (0, ))
    t2 = Thread(target=fib.addsun, args = (1, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
