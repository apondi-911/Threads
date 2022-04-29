# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from threading import *


def show():
    print("This is a child thread")


t = Thread(target=show())
t.start()
print("This is the parent thread")
