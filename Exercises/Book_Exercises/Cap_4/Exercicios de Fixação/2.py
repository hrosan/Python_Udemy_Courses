"""
Read three values and calculate their mean
"""
# Importing library
import random as rd
# Functions
def mean_value(*values):
    """
    mean_value
    This functions just returns a mean value
    Returns:
        float: The mean value of the given numbers
    """
    acc = 0 # An accumulator to sum up every item inside values
    for value in values:
        acc += value  # Summing every value given by the user
    return acc/len(values)

# Variables
variable1 = rd.randint(1,10)
variable2 = rd.randint(1,10)
variable3 = rd.randint(1,10)
variable4 = rd.randint(1,10)

print(f'Values: {variable1}, {variable2}, {variable3}, {variable4}')

# Results
# Calling a function
result = mean_value(variable1,variable2,variable3,variable4)
print(result)