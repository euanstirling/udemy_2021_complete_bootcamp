
#! STRING FORMATTING AND PRINTING

# todo LOOK AT PRINT FORMATING NOTEBOOK

# * To 'inject' a variable in to a string the simplest way in concatination

my_name = "jose"
print("hello " + my_name)


# * There are multiple ways to format strings for printing variables to them. This is known as string interpolation

# ! .format() method

# * Syntax:
# * "string {variableplaceholder1} then also {variableplaceholder2}".format("something1", "something2")

print("this is a string {}".format("INSERTED"))

# * Insert by Index Position

print("The {} {} {}".format("fox", "brown", "quick"))

print("The {2} {1} {0}".format("fox", "brown", "quick"))

print("The {0} {0} {0}".format("fox"))

# * Can also order by assigning them keywords. (Like a variable assignment)

print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

# * Float Formating follows "{value:width.precision f}"

result = 100/777
print(result)
print("The result was {r}".format(r=result))

# * In this example value is r, 1 is width, precision is 3 (3 decimal places)
print("The result was {r:1.3f}".format(r=result))

# * Width just tends to ad white space so is not too useful
print("The result was {r:10.3f}".format(r=result))

#! f strings Formatted string literals

name = "Jose"
print("Hello, his name is {}".format(name))
# * is changed to
print(f"Hello, his name is {name}")

name_2 = "Sam"
age = 3

print(f"{name_2} is {age} years old")
