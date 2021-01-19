import math

ans = (100 / 2) * 2 + 10 - 9.75
print(ans)

# 44 add the brackets and then multiply
# 29 multiplication before addition
# 34 multiplication before addition

# type will be a float
ans2 = 3 + 1.5 + 4
print(type(ans2))

# square root math.sqrt(int or float)
square_root = 100 ** 0.5
print(square_root)

square_root2 = math.sqrt(100)
print(square_root2)

# square is **
square = 10 ** 2
print(square)

#! Strings
s = "hello"
print(s[1])

print(s[::-1])

print(s[4])
print(s[-1])


#! Lists
list1 = [0]*3
print(list1)

list2 = [0, 0, 0]
print(list2)

# replace "hello" with goodbye
list3 = [1, 2, [3, 4, 'hello']]

list3[2][2] = "goodbye"
print(list3)

# * Sort the list 2 ways
list4 = [5, 3, 4, 6, 1]

# 1.
list4.sort()
print(list4)
# 2.
print(sorted(list4))


#! Dictionaries

# grab hello
d = {'simple_key': 'hello'}
print(d["simple_key"])

# grab hello
d = {'k1': {'k2': 'hello'}}
print(d["k1"]["k2"])

# grab hello
d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d["k1"][0]["nest_key"][1][0])

# grab hello
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d["k1"][2]["k2"][1]["tough"][2][0])

#! Tuples and Sets

# Tuples are immutable

my_tuple = (1, 2, 3)

# Sets are a list of unique values

list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]

print(set(list5))

# Booleans
False
False
False
True
False

# What is the boolean output of the cell block below?

# two nested lists
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
False
