#!/usr/local/bin/python

a = 22
b = 44
c = 55
d = None

if 22:
    print("This will be printed -> if 22:")

if "hello":
    print("This will be printed -> if hello:")

if 0:
    print("This will not be printed")

if d:
    print("This will not be printed")           # set to None (same as False) so not printed

print("Let us take a look at logical operators:")

if a and b and c:                   # and operator. If statement needs to evaluate to true for the print() to execute
    print("Printed -> if a and b and c:")

if a and b and c and d:             # will not print since all statements need to be True. The d = None makes print() not execute
    print("Not printed")

if a < b and a < c:
    print("a is smaller than b and c -> without braces")            # this will print since both conditions in if statement evaluate to True

if (a < b) and (a < c):
    print("a is smaller than b and c -> with braces")

if a or b or c or d:                    # any condition needs to be true for it to execute the print() statement
    print("This is printed -> if a or b or c or d :")

if not d:
    print("Not of d will be printed since None is True")        # None is only True because if not d reverses its operation (i.e. changes it from being False to True)


