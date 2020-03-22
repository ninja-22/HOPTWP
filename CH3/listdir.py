#!/usr/local/bin/python

import os

r = os.getcwd()
print(r)

print("Changing directory...")
os.chdir('/Users/ninja/Documents/HelloTest')
r = os.getcwd()
print(r)

print("Listing all directories...")
r = os.listdir('/Users/ninja/Documents/HelloTest')
print(r)