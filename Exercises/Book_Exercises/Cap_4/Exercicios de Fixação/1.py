"""
Leia 4 valores, calcule a soma entre eles e apresente o resultado
"""
# Library import
import random as rd

# Functions
def sum_values(value0,value1,value2,value3):
    return value0+value1+value2+value3

# Variables
v0 = rd.randint(1,10)
v1 = rd.randint(1,10)
v2 = rd.randint(1,10)
v3 = rd.randint(1,10)
print(f'values:{v0},{v1},{v2},{v3}')

# Calling th function
result = sum_values(v0,v1,v2,v3)
print(result)