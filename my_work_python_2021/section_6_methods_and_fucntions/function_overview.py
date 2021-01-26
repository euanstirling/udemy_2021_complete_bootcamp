
#! FUNCTION OVERVIEW

# Exercise solutions are below
# https://docs.google.com/document/d/181AMuP-V5VnSorl_q7p6BYd8mwXWBnsZY_sSPA8trfc/edit?usp=sharing

#!Exercise 9

def myfunc(*args):
    mylist = []
    for num in args:
        if num % 2 == 0:
            mylist.append(num)

    return(mylist)


print(myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


#! Exercise 10
#! Option 1
def myfunc2(string):
    new_string = ''
    for x in range(len(string)):
        if (x+1) % 2 == 0:
            new_string += string[x].upper()
        else:
            new_string += string[x].lower()
    return new_string


print(myfunc2("pearljam"))

#! Option 2


def myfunc3(x):
    out = []
    for i in range(len(x)):
        if i % 2 == 0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)


print(myfunc3("pearljam"))

#! Option 2 with names changed


def myfunc4(string):
    upperlowerstring = []
    for letter in range(len(string)):
        if letter % 2 == 0:
            upperlowerstring.append(string[letter].lower())
        else:
            upperlowerstring.append(string[letter].upper())
    return "".join(upperlowerstring)


print(myfunc4("pearljam"))
