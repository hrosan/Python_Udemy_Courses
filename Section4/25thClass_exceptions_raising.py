'''
 These examples demonstrate how you can use exception handling to detect and handle exceptional situations in 
your code. By raising specific exceptions, you can communicate error conditions and handle them appropriately in your 
program.
'''

'''
    In this example, we have a function calculate_average that calculates the average of a list of numbers. 
If the input list is empty, it raises a ValueError with a custom error message.
'''
# Raising an exception inside a function
def calculate_average(numbers):
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    total = sum(numbers)
    return total / len(numbers)

try:
    average = calculate_average([])
except ValueError as e:
    print("An error occurred:", str(e))

'''
    In this example below, we have a function validate_username that validates a username based on certain criteria. 
If the username has less than 3 characters or contains non-alphanumeric characters, it raises a ValueError with an 
appropriate error message.
'''
# Raising an exception based on a condition:
def validate_username(username):
    if len(username) < 3:
        raise ValueError("Username must have at least 3 characters")
    if not username.isalnum():
        raise ValueError("Username can only contain alphanumeric characters")

try:
    username = input("Enter your username: ")
    validate_username(username)
    print("Username is valid!")
except ValueError as e:
    print("An error occurred:", str(e))