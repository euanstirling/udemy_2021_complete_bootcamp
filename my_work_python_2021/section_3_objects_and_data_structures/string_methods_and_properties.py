
#! STRING METHODS AND PROPERTIES

# * Immutability

# * We would like to change the name Sam to Pam
#! name = "Sam"
#! name[0] = "P"

#! This does not work are 'str' object does not support item assignment

# * To do this, we need to concatinate using the slice function

name = "Sam"

# * First we would slice the letters "am" from Sam
last_letters = name[1:]
print(last_letters)

# * Then we Concatinate the last_letters variable with P to make Pam
print("P" + last_letters)

# * assign the variable
x = "Hello World, "

# * re assign the variable with the concatination
x = (x + "it is beautiful outside")

# * print the new variable x
print(x)


letter = "z"
print(letter * 10)

# ! Be careful with data type

# * This will print the 2 strings to make 23 not add the numbers
string_1 = "2" + "3"
print(string_1)

# * Built in string methods

string_2 = "Hello World"


print(string_2.upper())
print(string_2.lower())
# * This does not effect the original string, you would need to reassign it to do that
#! REMEMBER TO ADD () TO EXECUTE THE METHOD OR FUNCTION

# * split lets you create a list from a string
print(string_2.split())

string_3 = "hi, this is a string"
print(string_3.split())

# * You can split on any item in the string. TO split the string on the letter "i"
print(string_3.split("i"))

# * Capitalise the first letter of string
print(string_3.capitalize())

# * Count how many letter "h" are in the string
print(string_3.count("h"))

# * What index location is the letter "g"
print(string_3.find("g"))

# * Print the length of the string
print(len(string_3))
