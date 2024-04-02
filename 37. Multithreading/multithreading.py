# thread : a flow of execution. like a separate order of instructions.
#          However, each thread takes a turn running to achieve concurrency.
#          GIL(Global Interpreter Lock), allows only one thread to hold the control of the Python interpreter at any one time.

# cpu bound : program/task spends most of it's time waiting for internal events in the CPU (CPU intensive).
#             use multiprocessing

# io bound : program/task spends most of it's time waiting for external events (user input, file I/O, network I/O, web scraping).
#            use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print('You are done eating breakfast')

def drink_coffee():
    time.sleep(4)
    print('You are done drinking coffee')

def study():
    time.sleep(5)
    print('You are done studying')

# using threads
# create threads
x = threading.Thread(target=eat_breakfast, args=())
y = threading.Thread(target=drink_coffee, args=())
z = threading.Thread(target=study, args=())

# start threads
x.start()
y.start()
z.start()
# takes 5 seconds to complete all the tasks

# join threads -> makes the Main thread wait for the threads to finish, by then only 1 thread will be running, i.e. Main thread
x.join()
y.join()
z.join()
    
print(threading.active_count())
print(threading.enumerate())

# without using threads
# eat_breakfast()
# drink_coffee()
# study()
# takes 12 seconds to complete all the tasks