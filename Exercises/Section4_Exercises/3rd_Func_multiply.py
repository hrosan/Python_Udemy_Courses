'''
Create a function that double, triple and quadruple a given number
'''
import random as rd
# Function to multiplicate
def multiplicate(number_multiplicate=1,factor_to_multiplicate=1):
    outer_number = number_multiplicate*factor_to_multiplicate
    def inner_multiplication(inner_factor_multiplicator):
        number = outer_number*inner_factor_multiplicator 
        def multiply_by_four(inner_factor):
           return number*inner_factor
        return multiply_by_four # Second <Buffer>, waitinf for the next multiplicator value
    return inner_multiplication # <Buffer> return its inner function, but it still waiting



# First create a variable to multiply
number_to_multiply = rd.randint(1,10) # A random number from 1 to 10
double_number = multiplicate(number_to_multiply,2)
triple_number = double_number(3)
quadruple_number = triple_number(4)
# OUTPUT: It'll show: number_to_multiply, <inner_multiplication address>, 
#                     inner_multiplication return
print(number_to_multiply, quadruple_number)