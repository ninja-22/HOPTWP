#!/usr/local/bin/python

def expressions():
    gen_obj = (x*x for x in range(3))
    for x in gen_obj:
        print(x)

expressions()