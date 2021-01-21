
#! LIST COMPREHENSION
# * Unique way of quickly creating a list with Python
# * These can be used if you find yourself using a for loop along with .append() to create a list

mystring = "hello"

mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

# * more efficient way

mystring2 = "goodbye"

# * Flattened out FOR loop
# element FOR element IN (some for of string, object, list)

# like a FOR loop, element can be anything
mylist2 = [letter for letter in mystring2]

print(mylist2)

# eg

mylist3 = [num for num in range(1, 11)]
print(mylist3)

# you can perform operations on first variable name
# eg from example above

# this will square all the items in the created list
mylist4 = [num**2 for num in range(1, 11)]
print(mylist4)

# can also add in IF stratements
# eg to check take all the even numbers

mylist5 = [number for number in range(0, 11) if number % 2 == 0]
print(mylist5)

celcius = [0, 10, 20, 34.5]

fahrenheit = [((9/5) * temp + 32) for temp in celcius]
print(fahrenheit)

# same example in a FOR loop
fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5) * temp + 32))

print(fahrenheit)
print(fahrenheit[3])  # last elelment in the list
print(fahrenheit[-1])

# todo look at example for list2, list3 and list4 and work re-write as a regular FOR loop
