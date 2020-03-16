#!/usr/local/bin/python

print("----- Iterate over strings -----")
my_str = "Hello"
for s in my_str:
    print(s)

print("----- Iterate over lists -----")
my_list = [1, 2, 3, 4]
for b in my_list:
    print(b)

print("----- Iterate over lists with index number -----")
my_list = [1, 2, 3, 4]
for index, value in enumerate(my_list):
    print(index, value)

print("----- Iterate over lists with dictionary keys -----")
my_dict = {"Name": "Uthman", "Location": "Manchester/London", "Age": "23"}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

print("----- Iterate over lists with dictionary with items() -----")
my_dict = {"Name": "Uthman", "Location": "Manchester/London", "Age": "23"}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

print("----- Iterate over tuples -----")
my_tuple = ()