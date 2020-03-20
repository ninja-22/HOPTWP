#!/usr/local/bin/python

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

zipper = list(zip(l1, l2))          # takes two lists or iterables and aggregates the elements, returning a tuple iterator
print(f"The zipped list is: {zipper}")

sum = [x+y for x,y in zipper]           # sum of generated tuple in zipper e.g. (1, 5) would be [6] - the first item in the list
print(f"The sum is: {sum}")

sum_1 = list(map(lambda x: x[0] + x[1], zip(l1, l2)))       # achieves same as above with different code
print(f"Sum one: {sum_1}")

sum_2 = [x+y for x, y in zip(l1, l2)]                   # achieves same as above with different code 
print(f"Sum two: {sum_2}")


