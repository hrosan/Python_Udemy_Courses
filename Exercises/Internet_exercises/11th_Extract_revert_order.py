'''
Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space 
separating the digits.
'''
import random
while True:
    # Initializing Variables
    random_integer = random.randint(1000,10000000)  # Use the randint number
    cast_to_string = "" # Variable to receive the random number
    string_accumulator = ""
    print(random_integer)
    # Casting the type of the variable
    cast_to_string = str(random_integer) # Turning the int number into string
    # Getting the lenght of random number <4 to 8>
    i = len(cast_to_string)
    # Reversing the number and adding an " "
    while i > 0:
        string_accumulator += cast_to_string[i-1]+" "
        i -= 1
    print(string_accumulator)
    break
    
