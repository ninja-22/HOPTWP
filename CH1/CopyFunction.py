import copy


list1 = ["Hello", 1, 2, 3]
print(list1)                    # print the list without any changes

a = copy.copy(list1)            # copy the list using the copy function, access it using variable a
a[0] = 0                        # add 0 to index 0. This replaces "Hello" with 0

print(a)                        # this has changed
print(list1)                    # this has not changed

