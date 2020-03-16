#!/usr/local/bin/python

a = 22;b = 44;c = 55; d = None

if a and b and c and d:
    print("All not none")

elif b and c and d:
    print("A seems to be none")

elif a and c and d:
    print("B seems to be None")

elif a and b and d:
    print("C seems to be None")

elif a and b and c:
    print("D seems to be None")         # only this is printed since D is actually = to None

else:
    print("That is strange!")