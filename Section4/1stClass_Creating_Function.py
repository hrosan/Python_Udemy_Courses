'''
Functions in Python are blocks of reusable code that perform a specific task. 
They allow you to break down your program into smaller, modular pieces, 
making your code more organized, easier to understand, and reusable.
'''

# Function Definition
def greet():
    print("Hello, world!")

# Function Call
greet()  # Function call

# Function with Parameters and Arguments
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")  # Passing "Alice" as an argument to the greet function

# Function with Return Statement
def add(a, b):
    return a + b

result = add(3, 5)  # Calling the add function and assigning the result to the "result" variable

# Function Documentation
def multiply(a, b):
    """
    Multiply two numbers and return the result.

    Parameters:
    - a: The first number (int or float).
    - b: The second number (int or float).

    Returns:
    The product of a and b.
    """
    return a * b