'''
Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.
The factorial (symbol: !) means to multiply all whole numbers from the chosen number 
down to 1.
'''
from random import randrange

while True:
    n_factor = 0 # Number that the factorial will be calculated
    fac_string = "" # Just to show the string in the prompt
    j = 1 # Neutral element in the multiplication
    # Inputing a number to the variable
    n_factor = randrange(3,10) # The variable will go from 1 to 6 randomly
    # Calculating the factorial
    for i in range(1,n_factor+1):
        j *= i # Calculating the factorial of a number
        # CASES TO PRINT THE CALC
        if i < n_factor: # While i < n_factor 
            fac_string += str(i)+"x" # it concatenate the numbers with a times string
        elif i == n_factor: # at the end when i == n_factor
            fac_string += str(i) # remove the times sign e puth just the last string
    print(f'{n_factor}! > {fac_string} = {j}') # print the string how it was calculate
    break
