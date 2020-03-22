#!/usr/local/bin/python

def main():
    num_1 = input("Enter the first number: ")
    num_2 = input("Enter the second number: ")
    sum_ = num_1 + num_2
    print(f"The sum of the two numbers is: {sum_}")             # returns a string so it concatenates the two inputs e.g. first = 2 and second = 2, the sum is displayed as 22 because these are strings
    print(f"This returns a string: {type(sum_)}")
    print(f"Actual sum: {int(num_1) + int(num_2)}")         # conversion to integer type so the sum is calculated properly


main()