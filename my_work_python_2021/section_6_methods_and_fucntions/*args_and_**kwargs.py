
#! *ARGS and **KWARGS (arguments and keyword arguments)

def myfunc(a, b):
    # returns 5% of the sum of a and b
    return sum((a, b)) * 0.05


print(myfunc(40, 60))
# * these are positional arguments, 40 = a as it is in the first position, b = 60 as it is in the second position
# * We have to pass the arguments in as a tuple

#! What if we want to work with more than 2 numbers??

# we could assign al;ot of paramenters


def myfunc2(a, b, c=0, d=0, e=0, f=0):
    # returns 5% of the sum of a and b
    return sum((a, b, c, d, e)) * 0.05


print(myfunc2(40, 60, 100, 200, 10, 50))
# you can't add more arguments than there are positional parameters

# * You can use *args to set your function to take an arbitrary number of arguments


def myfunc3(*args):
    return sum(args) * 0.05


# * this takes all the arguments and sets them inside a tuple no mmatter how many there are
print(myfunc3(2, 3, 4, 5, 6, 7, 8, 9))

# * You can print out the tuple


def myfunc4(*ARGS):
    print(ARGS)


# You do not need to use the word "args" You can call it anything. We just use args by convention. You just need to make sure it is used with the *
myfunc4(2, 3, 4, 5)

# * You can add the args tuple into a FOR loop


def myfunc5(*ARGS):
    for item in ARGS:
        print(item)


myfunc5(10, 100, 1000, 10000)

#! There is also a way to handle an arbitrary number of keyword arguments
# * we use **kwargs and this builds a dictionary of key value pairs


def myfunc6(**kwargs):
    print(kwargs)
    '''keyword args returns back a dictionary'''

    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find fruit here")


myfunc6(fruit="apple", vegetable="carrot", grain="barley")


#! These can be used in combination

def myfunc7(*ARGS, **KWARGS):
    print(ARGS)
    print(KWARGS)
    print("I would like {} {} ".format(ARGS[0], KWARGS["food"]))


myfunc7(10, 20, 30, fruit="orange", food="eggs", animal="dog")

# * When calling the function, we need to  ake sure we put the args and kwargs in the correct order. In the above example, the args are before the kwargs. This is the same order to when we declared the fucntion
