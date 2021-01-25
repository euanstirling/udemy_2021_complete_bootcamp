
#! INTRO TO FUNCTIONS

# * Functions allow us to create blocks of code that can easily be executed many times, without needing to constantly reqrite the entire bloock of code

# * Very important to get practice combining everything we have learnt so for. (control flow, loops, etc)

# * Creating a fumction requires a very specific syntax, including the "def" keyword, correct indentation and proper structure

# def tells python I am about to write a function
# The fucntion name should be in snake casing (lowercase with underscores)
# the paranthesis should be included at the end. This is where we will pass in arguments or parameters to the function
# Argumemts are just words saying "take these variables and pass it in to the function in order to work with it within the function"
# ":" A colon indicates an upcoming indented block. Everything indented is then inside the function
# Optional: multi-line string to describe function (it should be in triple quotes)
# You then add all the intended code within the funiction. Rmemebering it should all be indented
# You then call the code by using "name_of_function()"

def name_of_function():
    """ Docstring explains function """

    print("Hello")


name_of_function()

# !Generally you should use the "return" keyword inside the function instead of just printing it out. This allows us to assign the output of the function to a new variable

# eg. new function called "add_function" takes in 2 paramenters called num1 and num2 (these parameters can be called anything)
# It will "return" the result of num1 + num2
# "return" will allow us to save the result to a "variable" called "result" This variable could then be used elswhere in our code


def add_function(num1, num2):
    return num1 + num2


result = add_function(1, 2)
print(result)
