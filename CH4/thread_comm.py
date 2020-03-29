import threading
import time
import logging
logging.basicConfig(level = logging.DEBUG, format = '(%(threadName) - 10s) %(message)s',)

counter = 0
class Communicate():
    def __init__(self):
        pass
    def wait_for_event(self, e):
        global counter
        logging.debug("Wait for counter to become 5")
        is_set = e.wait()
        logging.debug(f"Yay! Now the counter has become {counter}")

    def increment_counter(self, e, wait_time):
        global counter
        while counter < 10:
            logging.debug("About to increment the counter")
            if e.is_set() ==False:
                e.wait(wait_time)
            else:
                time.sleep(1)
            counter = counter + 1
            logging.debug(f"Counter incremented: {counter}")
            if counter == 5:
                e.set()

obj = Communicate()
e = threading.Event()
t1 = threading.Thread(name = "Thread 1", target = obj.wait_for_event, args = (e,))
t2 = threading.Thread(name = "Thread 2", target = obj.increment_counter, args = (e, 1))
t1.start()
t2.start()


## above example shows how two threads can communicate with one another, thread 1 starts and waits for the counter to reach 5
# whilst thread 2 is operating at the same time (a counter from 0 to 10). Once thread 2 reaches 5, thread 1 will interrupt
# execution and run line 14. Then thread 2 will continue until the counter reaches 10, and the thread is closed 