#!/usr/local/bin/python

import child as c                # name of what you are importing is assigned to __name__ (the name of the .py file)
def parent_method():
    print("-----------------------")
    print("IN parent method - Invoking child()")
    c.child_method()
    print("-----------------------")

parent_method()