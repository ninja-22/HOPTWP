#!/usr/local/bin/python

print("----- For loop with range default start -----")
for i in range(5):
    print(f"Statement: {i}, step 1")


print("----- For loop with range specifying start and end -----")
for i in range(5, 10):
    print(f"Statement: {i}, step 1")

print("----- For loop with range specifying start, end, and step -----")
step = 2
for i in range (1, 10, step):
    print(f"Statement: {i}, step: {step}")

