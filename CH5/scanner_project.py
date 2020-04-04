#!/usr/local/bin/python3.7

import subprocess as sp
import os

class NmapPy():
    def __init__(self, command = []):
        b = input("Enter a hostname: ")
        self.command = command
        command.insert(3, b)

    def scan(self):
        try:
            p = sp.Popen(self.command, shell=False)
            p.communicate()
        except Exception as ex:
            print(f"Exception caught: {ex}")

nmap = NmapPy(["nmap", "-Pn", "-sV"])
nmap.scan()



# TO-DO
# Any hostname, not hardcoded into the program
# Loop "Try again." until a valid hostname/ip format is given i.e.  string or int.int.int.int
# Always append b to the end of the list instead of 3rd index