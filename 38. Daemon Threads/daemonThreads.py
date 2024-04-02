# daemon thread : a thread that runs in the background, not important for the main program to run.
#                 your program will not wait for the daemon threads to complete before exiting.
#                 non-daemon threads cannot normally be killed, stay alive until task is complete.

#                 eg. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for ", count, " seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.daemon = True

answer = input("Do you wish to exit?")