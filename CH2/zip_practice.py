
l1 = [1, 2, 3]
l2 = [1, 2, 3]

cubed = list(map(lambda x: x[0] ** 3, zip(l1, l2)))
print(f"Cubed values are: {cubed}")

squared = list(x ** 2 for x, y in zip(l1, l2))
print(f"Squared values are: {squared}")

sum = list(map(lambda x: x[0] + x[1], zip(l1, l2)))
print(f"Sum of values are: {sum}")

division = list(map(lambda x: x[0] / x[1], zip(l1, l2)))
print(f"Division of values are: {division}")


l1.append(l2)

l1 = [1, 2, 3]
l2 = [1, 2, 3]

l3 = l1 + l2
print(l3)

addition = list(map(lambda x: x[0] + x[1], zip(l1, l2)))
print(f"Addition = {addition}")

d1 = {"Name":"Uthman", "Age":"22"}
d2 = {"Location": "Manchester/London", "Occupation": "Security Engineer"}

hello = list(zip(d1, d2))           # only zips up the dictionary keys by default
print(hello)

hello2 = list(zip(d1.items(), d2.items()))          # keys and value in tuple pair
print(hello2)

hello3 = list(zip(d1.values(), d2.values()))        # print the values in tuple pair
print(hello3)
