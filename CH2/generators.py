#!/usr/local/bin/python

def genmethod():
    a = 100
    for i in range(3):
        print(f"A before the increment: {a}")
        a = a + 1
        yield a
        print(f"A after the increment: {a}")

def driver():
    v = genmethod()
    next(v)
    print("----------------------------")
    next(v)
    print("----------------------------")
    next(v)
    print("----------------------------")

def driver_for():
    for a in genmethod():
        print(f"A is: {a}")
        print("----------------------------")

# driver_for() code is a better way to achieve what driver() does and is much cleaner

genmethod()
driver()
driver_for()
