'''
A higher-order function is a concept in programming where functions can take other functions 
as arguments and/or return functions as results. In other words, a higher-order function treats
functions as values that can be manipulated and operated upon, similar to any other data type.
'''

def apply_operation(operation, a, b):
    return operation(a, b)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result = apply_operation(add, 2, 3)
print(result)  # Output: 5

result = apply_operation(multiply, 2, 3)
print(result)  # Output: 6

'''
In this example, apply_operation is a higher-order function that takes an operation function as
an argument, along with two other values a and b. It then applies the operation function to the
arguments a and b and returns the result.
The add and multiply functions are passed as arguments to apply_operation, demonstrating how 
functions can be treated as values and passed around to be executed.
Higher-order functions are powerful because they enable code reusability and abstraction. They 
allow you to write more generic functions that can be customized with different operations 
depending on the context. This functional programming paradigm provides flexibility and 
modularity in your code.
'''