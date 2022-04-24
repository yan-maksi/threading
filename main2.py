import time
import constns
from constns import *


class WorkCount(threading.Thread):
    def run(self):
        """"Exercise: thread queue. Application that handles a queue of jobs in N=5 threads."""

        while True:
            # blocking or non-blocking the turn
            locker.acquire()

            # we assign it None so that the loop is not constant (could stop)
            job = None

            # Logic of application
            if len(queue) > 0:
                constns.counter += 1
                constns.our_counter += 1
                job = queue[0]
                queue[0:1] = []
            # Release a lock, only one thread proceeds when a release() call resets the state to unlocked
            locker.release()

            # If the program has no work, it performs the following actions
            if job is None:
                print(f'{current_thread.name} - the queue is over')
                break

            # The output of the result for the user
            print(f' {current_thread.name} - working on {constns.counter} ({constns.our_counter}) '
                  f' from {job[0]} sleep for {job[1]}')

            # Delay for the correct operation of the program
            time.sleep(job[1])

        return


if __name__ == '__main__':

    print(f'{thread.name} - start thread')

    # recalculation thread count
    for i in range(thread_count):
        threads.append(WorkCount())

    # Start the thread’s activity
    for thread in threads:
        thread.start()

    # Wait until the thread terminates
    for thread in threads:
        thread.join()
