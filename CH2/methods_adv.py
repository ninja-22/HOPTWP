#!/usr/local/bin/python

def method_1(*args):
    print("------------------------")
    print("Method_1 ")
    print(f"Received: {args}")
    sum = 0
    for arg in args:
        sum = sum + arg
    print(f"Sum: {sum}")
    print("------------------------")

def method_1_rev(a = 0, b = 0, c = 0, d = 0):
    print("------------------------")
    print("Method_1_rev")
    sum = a + b + c + d
    print(f"Sum: {sum}")
    print("------------------------")

def method_2(**args):
    print("------------------------")
    print("Method 2")
    print(f"Received: {args}")
    for k,v in args.items():
        print(f"Key: {k}, Value: {v}")
    print("------------------------")

def method_2_rev(k1 = "first key", k2 = "second key"):
    print("------------------------")
    print("Method_2_rev")
    print(f"Value for K1: {k1}")
    print(f"Value for K2: {k2}")
    print("------------------------")

def execute_all():
    method_1(1, 2, 3, 4, 5)
    method_2(k1 = 22, k2 = 33)
    my_list = [1, 2, 3, 4]
    my_dict = {"k1": "Value 1", "k2": "Value 2"}
    method_1_rev(*my_list)
    method_2_rev(**my_dict)


execute_all()