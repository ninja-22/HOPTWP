import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG, format = '(%(threadName) -10s) %(message)s',)
print("------------------------Demonic Threads Example------------------------")

class Threads():
    def __init__(self):
        pass

    def execute(self, type_):
        logging.debug(f"Enter: {type_}")
        time.sleep(4)
        logging.debug(f"Exit: {type_}")

obj = Threads()
t = threading.Thread(name = "D", target = obj.execute, args = ("Demonic",))    # name of the thread, target = method to be executed
t.setDaemon(True)
logging.debug("Main started")
t.start()
logging.debug("Main ended")