dict1 = {"Name": "Uthman", "Age": "23", "Location": "Manchester/London"}

print(dict1)  # print the dictionary

yo = dict1.get("Name", False)  # use get method to retrieve value from a key in dictionary. Second argument arbitrary and optional

hello = dict1["Name"]   # achieves the same result as the get() method

print(yo)
print(hello)

dict1["Sex"] = "Male"    # adding a new key to the dictionary

print(dict1)

tupleit = (1, 2, 3)
listit = [4, 5, 6]

dict1["tupleit"] = tupleit              # adding a tuple to the dictionary
dict1["listit"] = listit                # adding a list to the dictionary

print(dict1)

dict2 = {"Occupation": "Security Engineer"}

dict1.update(dict2)                     # merging the two dictionaries together

print(dict1)

print(dict1.keys())                            # retrieve all the keys from the dictionary
print(dict1.values())                          # retrieve all values from the dictionary

print(dict1.items())                           # used to iterate over key-value pairs. returns list class instance (list of tuples). This is a dictionary items class.

list(dict1.items())                         # convert the dict_items class into a list
print(f"The dictionary items class is of type: {type(list(dict1.items()))} and the full list is: {list(dict1.items())}")

def checker():
    if "Name" in dict1:
        print("True")
        print(f'The value is: {dict1.get("Name")}')
    else:
        print("Try again")

checker()

print(sorted(dict1.keys()))             # sort by keys
print(sorted(dict1.items()))            # sort by keys (list tuple output)
try:
    b = sorted(dict1.values())              # sort by values, throws TypeError in this case because the values list contains tuples (with numeric data types) and strings. Cannot sort the two
except:
    TypeError

del dict1["Occupation"]                 # use del and key name to delete specific key-value pair
print(dict1)

dict1.pop('Location')           # delete key-value pair using pop(). Pass the key as an argument.
print(dict1)

