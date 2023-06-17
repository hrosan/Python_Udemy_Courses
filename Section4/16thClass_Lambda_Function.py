'''
Lambda functions, also known as anonymous functions, are a way to create small, one-line 
functions without using the def keyword. They are typically used for simple and concise 
operations where a full function definition is not necessary.
'''

# The basic syntax of a lambda function is:
#       lambda arguments: expression

# Regular function
def square(x):
    return x ** 2

print(square(5))  # Output: 25

# Lambda function
square_lambda = lambda x: x ** 2

print(square_lambda(5))  # Output: 25
