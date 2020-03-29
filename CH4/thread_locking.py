import threading
import logging
import time
import random

logging.basicConfig(level = logging.DEBUG, format = '(%(threadName) - 10s) %(message)s',)

class ResourceControl():
    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()

    def increment_counter(self):
        self.lock.acquire()
        try:
            logging.debug(f"Acquired lock... {self.counter}")
            self.counter = self.counter + 1
        finally:
            logging.debug(f"Releasing lock... {self.counter}")
            self.lock.release()

    def execute(self):
        th = threading.currentThread()
        self.increment_counter()

    def start_threads(self, count):
        for i in range(count):
            t = threading.Thread(name = f"Thread_{i}", target = self.execute)
            t.start()


r = ResourceControl()
r.start_threads(5)
for t in threading.enumerate():
    if t is not threading.currentThread():
        t.join()
print(f"Counter value is: {r.counter}")

