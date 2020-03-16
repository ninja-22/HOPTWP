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


print("-------------------------------------------------------------------------------------------------------")
bit_wise = a & b

if bit_wise:
    print(f"Now bitwise AND returned non zero: {bit_wise}")         # printed since bit_wise = True. The else statement is not printed because this is
else:
    print(f"Again bitwise AND returned non zero: {bit_wise}")


print("-------------------------------------------------------------------------------------------------------")
bit_wise_or = a | c                 # | is the bitwise operator for OR

if bit_wise_or:
    print(f"Bitwise OR should return 2: {bit_wise_or}")         # returns 2 because that is True
else:
    print(f"That is strange --> {bit_wise_or}")                 # does not print


print("-------------------------------------------------------------------------------------------------------")
left_shift = a << b         # equivalent to a * 2^b = 2 * 2^2 = 2 * 4 = 8

if left_shift:
    print(f"Remember left shift has multiplication impact. -> {left_shift}")            # this will print 8
else:
    print(f"That is strange -> {left_shift}")

print("-------------------------------------------------------------------------------------------------------")
right_shift = a >> b        # equivalent to a / 2^b = 2 / 2^2 = 2 / 4 = 0.5 ----> this becomes 0

if right_shift:
    print(f"That is strange -> {right_shift}")
else:
    print(f"Remember right shift has division impact. -> {right_shift}")            # this will print 0

print("-------------------------------------------------------------------------------------------------------")
neg_minus_1 = ~ a    # the ~ means (-n-1), in this case (-a-1) = (-2-1) = -3
if neg_minus_1:
    print(f"~ operator has (-n-1) impact -> (-n-1) for {neg_minus_1} is: {neg_minus_1}")
else:
    print(f"~ operator has (-n-1) impact -> produced 0 -> {neg_minus_1}")



