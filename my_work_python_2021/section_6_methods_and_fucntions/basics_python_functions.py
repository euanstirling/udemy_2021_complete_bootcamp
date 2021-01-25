
#! PYTHON FUNCTION BASICS

def say_hello():
    print("hello")
    print("how")
    print("are")
    print("you")


say_hello()

#! REMEMBER THAT TO CALL A FUNCTION YOU NEED TO HAVE THE () IF THEY ARE NOT THERE, IT WILL RETURN THAT IT IS JUST A FUNCTION

# * You are most likely to be wanting to input some arguments or parameters to the function


def say_hello2(name):
    print(f"Hello {name}")


say_hello2("Jose")

# * The variable "name" could have been anyting, you would just need to make  sure it matches within the fucntion. It makes sense to call it something that is understandable

# If you forgot the argument, it would return an error saying we need to add an argument. To avoid the error, we need to add a "default" argument to the fucntion


def say_hello3(name="Default"):
    print(f"Hello {name}")


say_hello3()
# This will return a name of default but will still run effectively


def add_num(num1, num2):
    return num1 + num2


result = add_num(10, 20)
print(result)

# return allows you to save / assign the result as a variable


def print_result(a, b):
    print(a+b)


def return_result(a, b):
    return(a+b)


# this will return a NONE as we can assign a print to a variable. Print is not returning anything to be saved
# result2 = print_result(25, 75)

# print(result2)

result3 = return_result(100, 200)
print(result3)

# * You can add a print statement within a function if needed to see the output as well as return it. This can help with debugging  when  learning
