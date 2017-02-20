# import random

# create function and give random number variable and range between 1 and 10
    # create variable for number and range
    # return number

# create function variable to check the guess
    # create user input to enter in a number as an integer
    # if input matches number
        # print "sorry, you guessed wrong" and guess again
    # if input doesn't match number
        # print "congratulations"
# call function

import random

def guess_random(lower, upper):
    number = random.randint(lower, upper)
    return number

def check_guess():
    number_right = False
    computer_number = guess_random(1,10)
    correct = computer_number
    guesses_taken = 0
    while number_right == False:
        if guesses_taken >= 5:
            print("You ran out of guesses.")
            break
        user_guess = int(input("Enter a number between 1 and 10: "))
        if user_guess == correct:
            print("Congratulations! You guessed right in {} tries!".format(guesses_taken))
            number_right = True
        elif user_guess > correct:
            print("Too high. Guess again.")
        elif user_guess < correct:
            print("Too low. Guess again.")
        else:
            print("Sorry, you guessed wrong. Try again.")
        guesses_taken += 1
check_guess()
