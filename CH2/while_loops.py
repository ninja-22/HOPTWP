#!/usr/local/bin/python

i = 0
print("----- While Basics -----")

while i < 5:
    print(f"Without brackets: Statement {i}")           # while i < 5, print this statement and append the value of i to {i}, then add 1 and go to the beginning of while statement until while i < 5 evaluates to False
    i = i + 1

i = 0
while (i < 5):
    print(f"With brackets: Statement {i}")              # achieves the same result as above
    i = i + 1

print("----- While with Lists -----")
my_list = [1, 2, "a", "b", 33.33, "c", 4, 5, ["item1", "item2"]]
i = 0

while (i < len(my_list)):                    # while i < 9
    if (type(my_list[i]) == type(1)):
        print(f"Found integer: {my_list[i]}")
    elif (type(my_list[i]) == type("a")):
        print(f"Found string: {my_list[i]}")
    elif (type(my_list[i]) == type([])):
        print("----- Found inner list - now let us iterate: -----")
        j = 0
        while (j < len(my_list[i])):
            print(f"Inner item: {my_list[i][j]}")
            j = j + 1
    else:
        print(f"Neither integer nor string: {my_list[i]} and Type is: {type(my_list[i])}")
    i = i + 1
