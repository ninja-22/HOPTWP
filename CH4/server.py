#!/usr/local/bin/python

import socket

class SP():
    def server(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('192.168.0.5', 80))
            s.listen(1)
            while True:
                try:
                    c, addr = s.accept()
                    print(f"Got connection from: {addr}")
                    while True:
                        data = c.recv(1024)
                        if data:
                            d = data.decode('utf-8')
                            print(f"Got data: {d}")
                            c.send(str(f"ACK: {d}...").encode('utf-8'))
                        else:
                            print(f"No more data from the client: {addr}")
                            break
                finally:
                    c.close()
        except Exception as ex:
            print(f"Exception caught: {ex}")
            s.close()

obj = SP()
obj.server()