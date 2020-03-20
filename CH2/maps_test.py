#!/usr/local/bin/python

import math

def cubed(number):              # arbitrary "number" parameter passed to ensure that the function knows to expect 1 positional argument
    return number ** 3

ls = [3, 6, 7]
a = list(map(cubed, ls))
print(a)

