
#! DICTIONARIES
#! Unordered mappings for storing objects
#! Stored using key value values. Instead of knowing the index location you can call the key and it will return the value

# * Syntax: curly braces and colons signify the keys and the values
# * {"key1":"value". "key2":"value2"}

# * Dictionaries: Objects retrieved by key name
# *               Unordered and can not be sorted

# * Lists: Objects retrieved by location
# *        Ordered sequence and can be indexed or sliced

# * Contruct Dictionary

my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)

# * To get a value back, pass in the key using the square bracket

print(my_dict["key1"])

price_lookup = {"apple": "2.99", "oranges": "1.99", "milk": "5.80"}

print(price_lookup["apple"])

# * Very flexible in the data type they can hold. Can also hold lists or other dictionaries

d = {"k1": "123", "k2": [0, 1, 2], "k3": {"insideKey": 100}}

# * Get the list at k2
print(d["k2"])

# * Print the value of the insideKey. A dictionary inside a dictionary. Add another sqaure bracket to get to the next level within the dictionary (stacking index or key calls)
print(d["k3"]["insideKey"])

# * Print the 2 from the list
print(d["k2"][2])

# todo MAKE THE LETTER "c" UPPER CASE

d = {"key1": ["a", "b", "c"]}

# * Solution 1
my_list = d["key1"]
my_letter = my_list[2]
print(my_letter)
upper = (my_letter.upper())
print(upper)

# * Solution 2
my_upper = d["key1"][2].upper()
print(my_upper)

# * Add a key value pair to the dictionary

dict2 = {"k1": 100, "k2": 200}
dict2["k3"] = 300
print(dict2)

# * Overwrite existing key value pair

dict2["k1"] = "NEW VALUE"
print(dict2)

# * Useful dictionary methods

dict3 = {"key1": 100, "key2": 200, "key3": 300}

# * Return all the dictionary keys
dict3.keys()
print(dict3.keys())

# * Return all the values()
dict3.values()
print(dict3.values())

# * Return all pairing together (this will return a tuble)
dict3.items()
print(dict3.items())
