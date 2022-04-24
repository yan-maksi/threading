from time import sleep
from time import perf_counter
from threading import Thread


def main():
    print('Starting a task...')
    sleep(0.01)
    print('done')


# create two new threads
thread1 = Thread(target=main)
thread2 = Thread(target=main)

open_time = perf_counter()

# Start the thread’s activity
thread1.start()
thread2.start()

# Wait until the thread terminates
thread1.join()
thread2.join()

stop_time = perf_counter()
print(f'It took {stop_time - open_time: 0.2f} second(s) to complete.')
