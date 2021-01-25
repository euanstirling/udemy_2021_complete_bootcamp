
#! INTERACTIONS BETWEEN FUNCTIONS

from random import shuffle
#example = [1, 2, 3, 4, 5, 6, 7]

# this is happening in place so will not actually returnn a shuffled list
# shuffle(example)
# print(example)

#! SIMPLE 3 CUP GAME

mylist = ["", "O", ""]


def shuffle_list(mylist):
    # take in list and return shuffle version
    shuffle(mylist)

    return(mylist)


shuffle_list(mylist)


def player_guess():

    guess = ""

    while guess not in ["0", "1", "2"]:
        guess = input("pick a number: 0,1 or 2 ")

    return int(guess)


player_guess()


def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("Correct Guess!")
    else:
        print("Wrong, better luck next time!")
        print(mylist)


# Initial List
mylist = ["", "O", ""]

# Shuffle List
mixedup_list = shuffle_list(mylist)

# User Guess
guess = player_guess()

# Check Guess
# ------------------------
# notice how this function takes in the input based on the output of other functions
check_guess(mixedup_list, guess)
