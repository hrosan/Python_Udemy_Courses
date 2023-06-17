'''
Write a program that generates a random number between 1 and 100 and then lets the user
guess the number. The program should give the user a hint if their guess is too high or
too low, and should keep asking for guesses until the user guesses the correct number.
'''
from random import randint
# GENERATE RANDOM NUMBER
random_number = randint(0,11)
# USER GUESS
guess = int(input('Try to guess the number: '))
# WHILE-LOOP
while guess != random_number:
    print('WRONG GUESSING, TRY AGAIN')
    if guess > random_number: # CONDITION IF GUESS NUMBER IS HIGHER THAN RANDOM NUMBER
        print('Your guess is higher than the number!!')
    elif guess < random_number: # CONDITION IF GUESS NUMBER IS LOWER THAN RANDOM NUMBER
        print('Your number is smaller than the number!!')
    guess = int(input('Try to guess the number: '))
print('CONGRATS YOU GOT IT RIGHT')
