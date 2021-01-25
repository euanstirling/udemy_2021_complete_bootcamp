
#! LOGIC WITH PYTHON FUNCTIONS

def even_check(number):
    result = number % 2 == 0
    return result


print(even_check(20))

# you can write this as a one line function shown below


def even_check2(number):
    return number % 2 == 0


print(even_check2(21))


# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST

def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass

    return False

# CHECK INDENTATION - the "return False" needs to be outside of the for loop. This is so the for loop checks all the numbers in the list and then the function retuns False. If it was at the same level of indenetation as the for loop, the first number would return a True or False and the loop would stop


print(check_even_list([1, 3, 5, 7, 9, 10]))


def check_even_list2(num_list):
    # return all the even numbers in a list

    # placeholder variable
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass

    return even_numbers


print(check_even_list2([1, 2, 3, 4, 5, 6, 7, 8]))

# if all the numbers were odd, we would return an empty list
