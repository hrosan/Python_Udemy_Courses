'''
Packing arguments in Python allows a function to accept a variable number of arguments. 
It is done by using the * (asterisk) operator before the parameter name in the function 
definition. This allows the function to receive any number of arguments, which are packed 
into a tuple.

In any function definition, *args represents the packed arguments. 
You can use any name instead of args, but the * symbol is necessary to indicate packing.

When calling the function, you can pass any number of arguments, which will be automatically 
packed into the *args tuple. Inside the function, you can iterate over the packed arguments 
using a loop or perform operations on them as needed.

Packing arguments is useful when you want a function to be flexible and able to handle a 
variable number of inputs. It allows you to write functions that can accept different 
numbers of arguments without explicitly specifying them in the function definition.
'''
def sum_numbers(*args):
    """
    Example of a function that receives a packed argument and sums the numbers.

    Parameters:
    - *numbers: Variable number of numbers (int or float). It can be more than 1 argument

    Returns:
    The sum of the numbers.
    """
    total = sum(args)
    return total

result = sum_numbers(1, 2, 3, 4, 5) # Giving more than 1 element into the argument
print(result)  # Output: 15

def concatenate_strings(*strings):
    """
    Example of a function that receives a packed argument and concatenates the strings.

    Parameters:
    - *strings: Variable number of strings.

    Returns:
    The concatenated string.
    """
    result = ""
    for string in strings:
        result += string
    return result

result = concatenate_strings("Hello", " ", "World", "!")
print(result)  # Output: "Hello World!"

def find_max(*values):
    """
    Example of a function that receives a packed argument and finds the maximum value.

    Parameters:
    - *values: Variable number of values (int or float).

    Returns:
    The maximum value among the given values.
    """
    maximum = max(values)
    return maximum

result = find_max(10, 5, 8, 12, 3)
print(result)  # Output: 12