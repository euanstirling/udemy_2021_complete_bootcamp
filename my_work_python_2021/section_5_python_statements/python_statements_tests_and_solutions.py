
#! Use for, .split(), and if to create a Statement that will print out words that start with 's':

# * 1. st = 'Print only the words that start with s in this sentence'

st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == "s":
        print(word)

# * 2. Use range() to print all the even numbers from 0 to 10.

x = range(0, 11, 2)
for num in x:
    print(num)

# or

print(list(range(0, 11, 2)))

# * 3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

list = [x for x in range(1, 51) if x % 3 == 0]
print(list)

numbers = []
for num in range(1, 51, 1):
    if num % 3 == 0:
        numbers.append(num)
print(numbers)

# * 4. Go through the string below and if the length of a word is even print "even!"
# * st = 'Print every word in this sentence that has an even number of letters'

# * 5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# * 6. Use List Comprehension to create a list of the first letters of every word in the string below:
# * st = 'Create a list of the first letters of every word in this string'
