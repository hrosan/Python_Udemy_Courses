'''
try/except 
Is a Python control flow structure that allows you to catch and handle exceptions that may occur
during the execution of a program.
'''
# The general syntax for try/except is:

# try:
    # Code block where an exception might occur
# except ExceptionType:
    # Code block to handle the exception

'''
Here's how it works:

1. The try block contains the code that might raise an exception.
2. If an exception is raised in the try block, Python will look for an appropriate except block 
    to handle the exception.
3. If an appropriate except block is found, the code inside that block is executed. 
    This block should contain code that handles the exception, such as displaying an error message or taking corrective action to fix the problem.
4. If no appropriate except block is found, the program will terminate with an error message.
'''

# Basic example
try:
    a = 10
    b = 0
    c = a / b # Division by 0
except ZeroDivisionError:
    print("Error: Division by zero")

# Example with many except
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Error: Invalid input")
except ZeroDivisionError:
    print("Error: Division by zero")