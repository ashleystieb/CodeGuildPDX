# rock paper scissors with random choice
import random

keep_playing = True
while keep_playing == True:
    choices = ['rock', 'paper', 'scissors']
    user_one = input("Choose 'rock,' 'paper,' or 'scissors.': ")
    user_two = random.choice(choices)
    sentence = "{} beats {}. {} won."

# paper beats rock
    if user_one == "paper" and user_two == "rock":
        print(sentence.format("paper", "rock", "user one"))
        keep_playing = False

    elif user_two == "paper" and user_one == "rock":
        print(sentence.format("paper", "rock", "user two"))
        keep_playing = False


# scissors beats paper
    if user_one == "scissors" and user_two == "paper":
        print(sentence.format("scissors", "paper", "user one"))
        keep_playing = False

    elif user_two == "scissors" and user_one == "paper":
        print(sentence.format("scissors", "paper", "user two"))
        keep_playing = False


# rock beats scissors
    if user_one == "rock" and user_two == "scissors":
        print(sentence.format("rock", "scissors", "user one"))
        keep_playing = False

    elif user_two == "rock" and user_one == "scissors":
        print(sentence.format("rock", "scissors", "user two"))
        keep_playing = False

# tied game
    elif user_one == user_two:
        print("both users entered the same input. try again.")
        keep_playing = True
