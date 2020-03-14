#!//usr/local/bin/python

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[0:5])
print(my_list[5:])
print(my_list)
print(f"This was printed using slicing: {my_list[::]}")
print(f"This is the list with a step of 2: {my_list[::2]}")
print(f"This is a reverse of the list: {my_list[::-1]}")
print(f"This is a portion of the list in reverse order: {my_list[5:0:-1]}")

my_list.append([1, 2, 3])
print(my_list)

print(my_list[3])

other_list = ["hello", "world"]

my_list.append(other_list)
print(my_list)