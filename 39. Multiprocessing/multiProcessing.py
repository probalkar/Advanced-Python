# multiprocessing : running tasks in parallel on different cpu cores, bypasses GIL used for threading

# multiprocessing = better for cpu bound tasks(cpu heavy)
# multithreading = better for io bound tasks(waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count())

    # a = Process(target=counter, args=(100000000,))
    # a.start()
    # a.join()
    # 88714.3043943  seconds

    a = Process(target=counter, args=(25000000,))
    b = Process(target=counter, args=(25000000,))
    c = Process(target=counter, args=(25000000,))
    d = Process(target=counter, args=(25000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("Finished in: ", time.perf_counter(), " seconds")

if __name__ == "__main__":
    main()