#!/usr/local/bin/python

import socket

class SP():
    def client(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.0.5', 80))
            while True:
                data = input("Enter data to send to server: ")
                if not data:
                    break
                else:
                    s.send(data.encode('utf-8'))
                    reply = s.recv(1024).decode('utf-8')
                    print(f"{reply}")

            s.close()
        except Exception as ex:
            print(f"Exception caught: {ex}")

obj = SP()
obj.client()
