'''
In Python, when calling a function, 
you can pass arguments using either named or positional arguments.
'''
# Positional Arguments: These are arguments passed to a function based on their position 
# in the function call. 
# The values are matched to the function parameters in the order they are provided.

def greet(name, age):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

greet("Alice", 25)  # Positional arguments

# Named Arguments: Also known as keyword arguments,
# these are arguments passed to a function using the parameter name followed by an equals 
# sign (=) and the corresponding value. 
# They allow you to specify the values for specific parameters regardless of their position.

def greet(name, age):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

greet(age=25, name="Alice")  # Named arguments

'''
Named arguments provide flexibility when calling functions, 
as you can pass the arguments in any order as long as you explicitly specify the parameter name. 
This can make your code more readable and self-explanatory.
Note that when using named arguments, you can mix them with positional arguments. 
However, positional arguments must always come before named arguments in the function call.
'''