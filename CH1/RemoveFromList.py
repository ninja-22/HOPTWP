list1 = [1, 2, 3, 4, "Hello"]

list1.pop(
    3)              # pop() takes the index as an argument, so you can specify exactly which element you want to remove from the list

print(list1)  # removed 4 from the list

list1[3] = 4  # replace index 3 with 4 (replaces Hello with 4)

print(list1)

del list1[3]  # removing 4 from the list again, this time using the del function

print(list1)

#  delete entire list by adding del list1
