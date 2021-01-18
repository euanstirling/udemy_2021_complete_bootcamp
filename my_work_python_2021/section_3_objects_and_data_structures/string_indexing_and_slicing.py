
#! STRING INDEXING AND SLICING

# * INDEXING

mystring = "Hello World"

print(mystring[0])
print(mystring[8])

print(mystring)
mystring_2 = mystring[6]
print(mystring_2)

print(mystring[-1])  # * This grabs the last index position of the string


# * SLICING

mystring_3 = "abcdefghijk"

# * This will start at index 2 and go right to the end
print(mystring_3[2:])

# * This will start at index 0 and stop at 3. Output does not include the last item. It will output abc. Do upto but do not include
print(mystring_3[:3])

# * To grab a section within the middle of a string
print(mystring_3[3:7])
print(mystring_3[1:-1])

# * Step size

# * Grab from the start of the string to the end of the string
print(mystring_3[::])

# * Grab the hole string in steps of 2
print(mystring_3[::2])

# * Grab the hole string in steps of 3
print(mystring_3[::3])

# * Combine with a range and step size
print(mystring_3[2:7:2])

# * Reversing a string order. Start at the beginning to the end but run backwards
print(mystring_3[::-1])
