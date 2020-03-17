#!/usr/local/bin/python

def print_msg():
    print("Basic message printed")

def print_msg2(message):
    print(message)

def print_msg3(message, do_return):             # if there are multiple parameters that can be specified, you can specify them in any order
    print(message)
    if do_return == True:
        return True

def print_msg4(m, op1 = "Hello, world!", op2 = False):
    print("---------------------------------------")
    print(f"Mandatory argument: {m}")
    print(f"Optional argument 1: {op1}")
    print(f"Optional argument 2: {op2}")
    print("---------------------------------------")

def print_msg5(arg1, arg2, arg3):
    return arg1*2, arg2*2, arg3*2

if __name__ == "__main__":
    print_msg()
    print("---------------------------------------")
    print_msg2("This is a custom message")
    print("---------------------------------------")
    rt = print_msg3("This is for message 3 with return type", True)
    print(f"Return value is: {rt}")
    print("---------------------------------------")
    n_rt = print_msg3("This is for message 3 without return type", False)           # set to False so nothing is printed
    print(f"Return value is: {n_rt}")
    n_rt = print_msg3(True, "This is another message")              # different order
    print("---------------------------------------")
    print_msg4("Test Mandatory")
    print_msg4(1, 2)
    print_msg4(2, 3, 2)
    print_msg4(1, op1 = "Test")
    print_msg4(1, op2 = 33, op1 = 44)
    r = print_msg5(1, 2, 3)
    print(f"Type: {type(r)}, Values: {r[0]}, {r[1]}, {r[2]}")


