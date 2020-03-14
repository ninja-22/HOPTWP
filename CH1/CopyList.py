list1 = [1, 2, 3]
list2 = list1

print(list2)

list2[0] = "Hello"
print(list2)
print(list1)

print("--------------------------------------------------------------------")

copied = list1[::]       # always create a copy of the list using the slice function
copied[0] = 1

print(copied)            # new sliced list
print(list1)             # original list, as you can see - this is unchanged.

print("--------------------------------------------------------------------")


