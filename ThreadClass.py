import time
from threading import *


class Demo:
    def num(self):
        pass

    def double(self):
        pass

    def square(self):
        pass


def double():
    for i in range(1, 6):
        print("The num is :", 2 * i)
        time.sleep(0.2)


def num():
    for i in range(1, 6):
        print("The num is :", i)
        time.sleep(0.2)


def square():
    for i in range(1, 6):
        print("The num is :", i * i)
        time.sleep(0.2)


obj = Demo()
t1 = Thread(target=obj.num())
t2 = Thread(target=obj.double())
t3 = Thread(target=obj.square())

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()
time.sleep(0.2)

t1.join()
t2.join()
t3.join()
print("This is the main thread")
