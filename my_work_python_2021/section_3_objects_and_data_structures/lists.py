
#! Lists - Ordered sequences that can hold a variety of objects
#! They use [] brackets and commas to seperate the objects in the list [1, 2, 3, 4, 5, 6]
#! Lists support indexing and slicing, can be nested and have a variety of methods that can be called off them
#! APPEND, POP, SORT, REVERSE METHODS

my_list = [1, 2, 3]
# * Lists can contain a mixture of objects
my_list2 = ["STRING", 100, 23.2]

print(len(my_list))

# * You can use indexing on a list

my_list3 = ["one", "two", "three"]
print(my_list3[0])

# * You can also use slice in the same way
print(my_list3[1:])

# * Concatinate lists

my_list4 = ["four", "five", "six"]

print(my_list3 + my_list4)

# * could also create a new list by assigning to a variable

new_list = my_list3 + my_list4

print(new_list)


# * We can change and mutate a list using the index point

new_list[0] = "ONE ALL CAPS"
print(new_list)

#! There are many methods available to a list type list variable name . then hit required method

# * Add element to the end of a list

new_list.append("seven")
print(new_list)

# * (Append does effect the list, it is known as affecting in place - permanently changes the list

new_list.append("eight")
print(new_list)

# * Remove items from a list .pop By default the index position is [-1] The last position

new_list.pop()
print(new_list)

# * you can now save this popped item

popped_item = new_list.pop()
print(popped_item)

# * You can aslo remove an item by using pop([index_position])

new_list.pop(0)
print(new_list)

# * method .sort

different_letters = ["a", "e", "x", "b", "c"]
different_numbers = [4, 1, 8, 3]

different_letters.sort()
# * (this is an inplace method as it does not return anything. It just sorts the list in place)
# * If you were to create a variabel against this, it would return NONE. It can not be reasigned to somerthing else.
print(different_letters)


# * method .reverse

different_letters.reverse()
print(different_letters)


# * This will output a NONE result. We would need to return
print(different_numbers.sort())

new_numbers = different_numbers
print(new_numbers)


#! TO INDEX A NESTED LIST, YOU NEED TO ADD ANOTHER SET OF BRACKETS (see example)
# * If i wanted to grab 2 from
my_list5 = [1, 1, [1, 2]]
print(my_list5[2][1])
