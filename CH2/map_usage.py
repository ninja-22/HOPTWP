#!/usr/local/bin/python

def square(num):
    return num ** 2

l1 = [1, 2, 3, 4]
sq = list(map(square, l1))          # map function can be used to perform an operation on elements of a list. first argument is the function to be performed, second argument is
print(sq)
