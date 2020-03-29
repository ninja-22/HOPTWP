import threading
import time
import logging

print("------------------------Non-Demonic Threads Example------------------------")
class Threads():
    def __init__(self):
        pass

    def execute(self, type_):
        print(f"Enter: {type_}")
        time.sleep(10)
        print(f"Exit: {type_}")

obj = Threads()
t = threading.Thread(name = "ND", target = obj.execute, args = ("Non Demonic",))
print("Main started")
t.start()
print("Main ended")

