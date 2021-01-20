
#! FOR LOOPS

# Many objects in pyhton are "iterable" meaning we can iterate over every element in an object such as every element in a list or every character in a string
# We can use loops to execute a block of code for every iteration

# * ITERABLE - you can perform an action for every thing in that object (iterate over the object)
# * eg. iterate over every character in a string, every item in a list, every key in a dictionary

# Syntax of a FOR loop

my_iterable = [1, 2, 3]
for item_name in my_iterable:
    print(item_name)

# make a variable assignment ( in this example it is is a list) [could be anything you want]
my_iterable = [1, 2, 3]

# keyword "FOR" and then variable name for placeholder for every item in iterable object (in this example it would be the numbers in list)
# keyword "IN" anf then the variable name we chose (my_iterable)
# " for every item in the list [1,2,3]"
for item_name in my_iterable:

    # print the item_name
    print(item_name)

# Explore the concepts

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:  # (this variable (num) can be anything, (mylist) needs to be predefined
    print(num)

# * You should chose a variable name that is related to what is in the object
# * You do not need to return the exact element that is inside the object

for num in mylist:
    print("bollocks")  # this will print out "bollocks" 10 times

mylist2 = ["hello", "Euan", "Stirling"]

for words in mylist2:
    print(words)

for num in mylist:
    # check for even
    if num % 2 == 0:

        print(num)
    else:
        print(f"odd number: {num}")

#! WATCH THE INDENTATION - ALL ABOVE WILL EXECUTE IN THIS FOR LOOP.


list_sum = 0  # my intial sum is 0

for num in mylist:
    list_sum = list_sum + num
# for each number in mylist we take the old value for list_sum and add on current number and then reasign that value to list_sum. We do this for every number in that list

print(list_sum)
# once completed print out the final list_sum value. The print call is out of the loop (if the print was part of the for loop you would get a runnning tallie of the sum. Having print outside the loop means you only get the final total)

# todo sum the even numbers from the list

list_sum = 0

for num in mylist:
    if num % 2 == 0:
        list_sum = list_sum + num

print(list_sum)

#! LOOPS IN STRINGS

mystring = "Hello World"

for letter in mystring:  # ! DOES NOT NEED TO BE "LETTER" - CALL IT ANYTHING!!!!!!!!!!
    print(letter)

# * LOOP THROUGH A TUPLE
tup = (1, 2, 3)

for item in tup:
    print(item)

# you can supplement the variable name ("item" in example above) with a _
# This is good syntax if you are planning on using the variable name

for _ in tup:
    print(_)

mylist3 = [(1, 2), (3, 4), (5, 6), (7, 8)]

print(len(mylist3))

for item in mylist3:
    print(item)

#! TUPLE UNPACKING

for a, b in mylist3:  # create temporary variable name that looks like the tuple
    print(a)
    print(b)
# print variable "a" and then variable "b"
# duplicate the structure of the object you are looking at

mylist4 = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]

for a, b, c in mylist4:
    print(b)

#! LOOP THROUGH A DICTIONARY

d = {"k1": 1, "k2": 2, "k3": 3}

for value in d:
    print(value)

# * When you iterate through a dictionary you only get the keys

# * to also get the items you need to call the items and it will return TUPLE pairs

for value in d.items():
    print(value)

# * If we just the items, we can use the same TUPLE UNPACKING technique using the "items" method

for key, value in d.items():
    print(value)

# * or we can use the VALUE method
for value in d.values():
    print(value)
