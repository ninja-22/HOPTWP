#!/usr/local/bin/python

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

sq_even = [x**2 for x in l1 if x%2 == 0]
l_sum = [x + y for x in l1 for y in l2]
sq_values = [{x: x**2} for x in l1]

print(f"Even squares: {sq_even}")
print(f"Sum: {l_sum}")
print(f"Square dictionary: {sq_values}")

