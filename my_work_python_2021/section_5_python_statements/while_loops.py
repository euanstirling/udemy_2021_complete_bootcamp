
#! WHILE LOOPS

# * While loops will continue to execute a block of code WHILE some conidtion remains True

# * eg. WHILE my pool is not full, keep fu=illing  my pool with water
# * or WHILE my dogs are still hungry, keep feeding my dogs

# Suntax of a while loop

# while some_boolean_condition:  #* normally some sort of comparison or some variables condition remains true
# do something

# else:  # can also be combined with an else statement so "while" the statement is true do something, "else" do something different

x = 0

while x < 5:
    print(f"The current value of x is {x}")
    x = x + 1  # or write it as x += 1

else:
    print("x is not less than 5")

# so while x=0 it is lower less than 5, therfore we will print out the current value of x. This will stop when the value of x = 5. To do this we need to increase x each time it loops. This is done by adding      x = x + 1 (if you forget the increment on x you will get an infinite while loop. )


#! BREAK CONTINE AND PASS KEYWORD

# * BREAK - breaks out of the current closest enclosing loop
# * CONTINUE - Goes to the top of the closest enclosing loop
# * PASS - Does not at all

#! PASS KEYWORD - it does nothing, it allows your code to pass without causing a syntax error
y = [1, 2, 3]

for item in y:
    # leave
    pass
print("end of my script")

#! CONTINUE KEYWORD - Tells programme to go back to the top of the closest and closing loop. In this example, if letter is "a" go bak to the start of the loop and continue

mystring = "Sammy"

for letter in mystring:
    if letter == "a":
        continue
    print(letter)

    #! BREAK - breaks out of closest and closing loop. For this example, it will break the loop if the letter is "a"

for letter in mystring:
    if letter == "a":
        break
    print(letter)

# todo A while Loop that breaks mid way

z = 0

while z < 5:
    if z == 2:
        break
    print(z)
    z += 1
