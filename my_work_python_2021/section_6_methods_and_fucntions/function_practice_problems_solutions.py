
#! Function Practice problems - solutions

#! WARM UP PROLEMS
# todo LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5`

# * Solution 1

def lesser_of_two_evens(a, b):

    if a % 2 == 0 and b % 2 == 0:
        # both numbers are even
        if a < b:
            result = a
        else:
            result = b

    else:
        # one or both numbers are odd!
        if a > b:
            result = a
        else:
            result = b

    return result


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(3, 5))

# * Solution 2
# * We can use the MIN and MAX inbuilt functions


def lesser_of_two_evens2(a, b):

    if a % 2 == 0 and b % 2 == 0:
        # both numbers are even

        result = min(a, b)
        # could change this to return min(a,b) and remove "return result"
    else:
        # one or both numbers are odd!

        result = max(a, b)
        # could change this to return max(a,b) and remove "return result"
    return result


print(lesser_of_two_evens2(2, 4))
print(lesser_of_two_evens2(3, 5))


# todo ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

# * Solution 1
def animal_crackers(text):
    wordlist = text.split()
    # this makes first = to the word at index 0 once the split has happened
    first = wordlist[0]
    second = wordlist[1]

    # this comparing the first character of the first and second words
    return first[0] == second[0]


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

# * Solution 2


def animal_crackers2(text):
    # we should also be making the text all lower as a capital would provide a false bool
    wordlist = text.lower().split()

    # use a double index call on the two split words
    return wordlist[0][0] == wordlist[1][0]


print(animal_crackers2('Levelheaded Llama'))
print(animal_crackers2('Crazy Kangaroo'))


# todo MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

# * Solution 1
def makes_twenty(n1, n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))


# * Solution 2

def makes_twenty2(n1, n2):

    return (n1 + n2) == 20 or n1 == 20 or n2 == 20


print(makes_twenty2(20, 10))
print(makes_twenty2(12, 8))
print(makes_twenty2(2, 3))


#! LEVEL ONE PROBLEMS

# todo OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

# * Solution 1 - upper method
def old_macdonald(name):

    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest


print(old_macdonald("macdonald"))

# * Solution 2 - capitalize method


def old_macdonald2(name):

    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()


print(old_macdonald2("macdonald"))


# todo  MASTER YODA: Given a sentence, return a sentence with the words reversed

# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(text):
    # get a list of the words
    wordlist = text.split()
    # reverse the order of the words
    reverse_wordlist = wordlist[::-1]
    # use .join method the join the list in to a string
    return " ".join(reverse_wordlist)


print(master_yoda('I am home'))
print(master_yoda('We are ready'))


# todo ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):

    # use abs to see what the absuolute value is of a number
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
