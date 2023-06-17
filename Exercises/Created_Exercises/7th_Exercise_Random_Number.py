'''
Write a program that generates a random number between 1 and 100 and then lets the user guess the number.
The program should keep asking the user for guesses until they guess the correct number.
'''
# Importing the library
import random
# Generating a random number
number_guessing = random.randint(0,101) # Allocating a random number in a variable
# User input to guess the number
player_guess = int(input('Guess the number: ')) # Input the number to guess
while (number_guessing != player_guess):
    print('Wrong Choice, you have other choice')
    player_guess = int(input('Guess the number: ')) # Input the number to guess
