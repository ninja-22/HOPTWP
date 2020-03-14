list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend([7, 8, 9])

print(f"This is the merged list using the extend method: {list1}")
print(f"This is the merged list using concatenation: {list1 + list2}")