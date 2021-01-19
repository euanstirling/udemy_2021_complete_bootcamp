
#! TUPLES

# * Very similar to lists however they have one key difference - immutability

# * Once an element in inside a tuple, it can not be reassigned

# * Tuples use parenthesis eg: (1,2,3)

t = (1, 2, 3)
mylist = [1, 2, 3]

print(type(t))
print(type(mylist))

print(len(t))

# * You can use different object types in a tuple
# * Can use index ansd slicing in a tuple

print(t[1])
print(t[-1])

# * 2 Built in methods for tuples (count and index)

t2 = ("a", "a", "c")

# * Will return how may occurances there are of "a" in the tuple
print(t2.count("a"))

# * Will return the index location of the first instance of "a" in the tuple
print(t2.index("a"))
print(t2.index("c"))

#! TUPLE IS IMMUTABLE. YOU CAN NOT REASSIGN ONCE IN THE TUPLE

# * mylist with a reasigned value at index [0]
mylist[0] = "new"
print(mylist)

# * t2 with an error on reassigning value at index [0]
# t2[0] = "new"
# print(t2)


#! TUPLES ARE MAINLY USED FOR PASSING AROUND OBJECTS IN PROGRAMME AND YOU NEED TO MAKE SURE THEY DONT GET CHANGED BY ACCIDENT
