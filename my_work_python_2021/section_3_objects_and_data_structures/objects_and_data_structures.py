
#! OBJECTS AND DATA STRUCTURES

# * Assigning a variable name
# * use lower case and avoid keywords like list and str (editor will highlight a key word if used)


# * You can reasign variables to different data types
my_dogs = 2
my_dogs = ["sammy", "frankie"]
#! You need to be aware of type()

# a = 5
# a = 10
# a = a + a
# print(a)
# print(type(a))


# * Assign varaibles and apply logic
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)


# * Because strings are ordered sequences it means we can use indexing and slicing to grab sub-sections of the string. We use [] to refer to index location

# * You can also use reverse indexing (last letter would be -1)
# * Slicing - grab a subsection of multiple characters
# * [start:stop:stop]
# * start is a numerical index for the slice start
# * stop is the index you go up to but not include
# * step is the size of the jump you take


print('this is also a string')
print("I'm going on a run")

print("hello world one")
print("hellow world two")

print("hello \nworld")  # * \n formats onto next line
# * \t formats a tab into the string \n\t is new line and a tab
print("hello \n\tworld")

# * Lenght of a string (includes all characters including spaces)

print(len("I 'am"))
