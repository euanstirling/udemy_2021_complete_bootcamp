
#! IF, ELIF and ELSE STATEMENTS

# We want certain code tto execute when a particular condition has been met
# eg IF my dog is hungry (some condition) then i will feed the fog (some action)

# * Control Flow syntax make use of colons and indentation (white space)
# * This indentation system is crucial to Python and is what sets it apart from other languages

# if statement syntax
# * if some_condition:
# execute some code
# * elif some_other_condition:
# do something different (you can have as many elif's as you want)
# * else:
# do something else

if True:
    print("it's true")

if 3 > 2:
    print("it's true")

hungry = True
if hungry:
    print("feed me know!")

hungry = False
if hungry:
    print("feed me know!")
else:
    print("I need nothing!")

# eg 1
loc = "Bank"

if loc == "auto shop":
    print("cars are cool")

elif loc == "Bank":
    print("money is cool")

elif loc == "Store":
    print("Welcome to the store")

else:
    print("I do not know much")

# eg 2
name = "john"

if name == "frankie":
    print("hello frankie")

elif name == "sammy":
    print("hello sammy")

elif name == "john":
    print("how is it going John?")

else:
    print("what is your name")
