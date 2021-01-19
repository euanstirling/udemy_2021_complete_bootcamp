
#! SETS
#! Unordered collections of unique elements
#! There can be only one representative of the saem object

myset = set()
print(myset)

myset.add(1)
print(myset)

# * It will look like a dictionary as it outputs in {} but it is not as it does not contaona ny key value pairs

myset.add(2)
print(myset)

# * try to add 2 again
myset.add(2)
print(myset)

# * The set will recognise there is already a 2 and leave to output as {1, 2}

# * Create a list with several repeated values and cast to a list so we can see only the unique values

mylist = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 33, ]

myset2 = set(mylist)
print(myset2)
