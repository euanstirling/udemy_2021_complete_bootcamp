

#! USEFUL OPERATORS

# built in functions and useful keywords

# ! RANGE
# * The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# * Syntax: range(start, stop, step)
# Parameter	      Description
# start	          Optional. An integer number specifying at which position to start. Default is 0
# stop	          Required. An integer number specifying at which position to stop (not included).
# step	          Optional. An integer number specifying the incrementation. Default is 1

from random import randint
import random
from random import shuffle
x = range(6)
for n in x:
    print(n)

x = range(3, 6)
for n in x:
    print(n)

x = range(3, 10, 3)  # includes the step size
for n in x:
    print(n)

for num in range(15):  # will print the range up to but not including 15
    print(num)

list(range(0, 10, 2))  # more efficient #todo CHECK THIS WORKS CORRECTLY

#! ENNUMERATE

# * The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# * The enumerate() function adds a counter as the key of the enumerate object.

# * Syntax: enumerate(iterable, start)
# Parameter	   Description
# iterable	   An iterable object
# start	       A Number. Defining the start number of the enumerate object. Default 0

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))

# eg

index_count = 0
for letter in "abcde":
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1

# because this operation is so common, there is an inbuilt method to so this called enumerate

word = "abcde"
for item in enumerate(word):
    print(item)
# this returns tuples

# we can then do tuple unpacking as per info in for_loops.py file
for index, character in enumerate(word):
    print(index)
    print(character)
    print("\n")


#! ZIP FUNCTION = zips together 2 lists

# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

# * Syntax: zip(iterator1, iterator2, iterator3 ...)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

mylist1 = [1, 2, 3]
mylist2 = ["a", "b", "c"]

# print(zip(mylist1, mylist2)) this just returns an notification that there is a zip in memeory

for item in zip(mylist1, mylist2):
    print(item)

new_list = list(zip(mylist1, mylist2))
print(new_list)
# this again retuns tuples. These can then be unpacked as per previous

#! MIN / MAX

# The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.
# * Syntax: min(n1, n2, n3, ...) or min(iterable)
# The max() function returns the item with the highest value, or the item with the highest value in an iterable.
# * Syntax: max(n1, n2, n3, ...) or max(iterable)

# If the values are strings, an alphabetically comparison is done.

mylist3 = [10, 20, 30, 40, 50]

print(min(mylist3))
print(max(mylist3))

#! RANDOM IMPORT

# you can import the random library by typing "from random import" and then select option/function

# The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
# * Syntax: random.shuffle(sequence, function)
# Note: This method changes the original list, it does not return a new list.

mylist4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist4)
print(mylist4)

#! GRABBING RANDOM INTEGER

# The randint() method returns an integer number selected element from the specified range.
# * Syntax: random.randint(start, stop)
# Note: This method is an alias for randrange(start, stop+1).

print(random.randint(3, 9))

print(randint(0, 100))

#! USER INPUT

# The input() function allows user input.
# * input(prompt)
# Input accepts everything as a string. You would need to convert to int, float if needed

result = input("enter a number here: ")
result2 = int(result)
print(result2)
print(type(result2))
