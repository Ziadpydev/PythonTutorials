from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello",i+1)
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi",i+1)
            sleep(1)

t1=Hello()
t2=Hi()

t1.start()
sleep(0.2)      #to avoid collision
t2.start()

#to run code only after threads have stopped
t1.join()
t2.join()
#when t1 t2 finishes then it runs
print("Bye")