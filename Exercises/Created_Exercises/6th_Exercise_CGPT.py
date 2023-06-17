'''Write a program that asks the user to enter a number and then prints out the sum of all the numbers
from 1 to that number.'''

# TYPING THE NUMBER
user_number = input("Enter a number: ")

# Casting the entry-data
int_user_number = int(user_number)

i = 0 # iterator for the sum
sum_iterator = 0 # accumulator

# While-loop
while i != int_user_number+1: # Condition to stop the while loop
    print(f"Sum: {sum_iterator} + {i} = ",sum_iterator+i) # Printing the sum
    sum_iterator += i # Accumulator
    i += 1
    if sum_iterator > 100: # Case if sum_iterator reach a certain value
        break # Exit the loop