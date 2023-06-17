'''The input() function in Python is a built-in function that prompts the user to enter input from the keyboard.
It takes an optional argument, args, which is a string that is displayed to the user as a prompt.'''

# Here's an example of how to use the input() function:
name = '' # declaring name as a string

name = input("What's your name? ") # Asking for a name ang allocating the name inside the variable name
print(f'Hello {name}!') # Printing a message in the prompt

'''
Note that the input() function always returns a string, even if the user enters a number. 
If you need to convert the user's input to a different data type, such as an integer or a float,
 you can use the appropriate type conversion function, such as int() or float()
'''

age = int(input("What is your age? ")) #the int() function is used to convert the user's input to an integer.
print(type(age))