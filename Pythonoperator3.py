# Write a program to illustrate the use of 'is' identity operator
a = 10
if type(a ) is int:
    print ("this is an integer")
else:
    print ("this is not an integer")
# Write a program to apply the right shift and left shift bitwise operator.
a = int(input("enter the number"))
left_shift = a << 2 
right_shift = a >> 2
print ("left shift", left_shift)
print ("right shift", right_shift)