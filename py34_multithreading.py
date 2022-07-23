# Running several threads is similar to running several different programs concurrently
# Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.
# Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.

from time import sleep
from threading import *


class Thread1(Thread):
    def run(self): # run() method is the entry point for a thread.
        for i in range(10):
            print(' print thread 1')
            sleep(1)
            
            
class Thread2(Thread):
    def run(self): # run() method is the entry point for a thread.
        for i in range(10):
            print(' print thread 2')
            sleep(1)
            
            
t1 = Thread1()
t2 = Thread2()

# t1.run()
# t2.run()
t1.start() # start() method starts a thread by calling the run method.
sleep(1)
t2.start() # start() method starts a thread by calling the run method.


t1.join() # join() waits for threads to terminate.
t2.join() # join() waits for threads to terminate.

print('Exit Form Main Thread')