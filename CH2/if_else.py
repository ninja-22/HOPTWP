#!/usr/local/bin/python

a = 22;b = 44;c = 55;d = None

if a and b and c and d:
    print("Not printed")                # not printed because all AND conditions need to be True. d = None, which equals False. So the line is not printed.

else:
    print("Remember the AND operator --> All must evaluate to True!")

if a == b:
    print("a and b are equal")      # not printed

else:
    print("a and b are not equal! But we can see how to use == :)")

print("-------------------------------------------------------------------------------------------------------")
print("\nLet's use some bitwise operators with conditional statements: \n")

a = 2;b = 2; c = 0
bit_wise = a & b & c

if bit_wise:                            # if bit_wise = True, print the statement below
    print(f"Now bitwise AND returned non zero: {bit_wise}")                 # not printed

else:
    print(f"Bitwise AND returned zero: {bit_wise}")             # printed since bit_wise is not True (because c = 0)

bit_wise = a & b

if bit_wise:
    print(f"Now bitwise AND returned non zero: {bit_wise}")         # printed since bit_wise = True. The else statement is not printed because this is

else:
    print(f"Again bitwise AND returned non zero: {bit_wise}")

