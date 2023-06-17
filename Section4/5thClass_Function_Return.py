'''
Function's value return
'''

# Declarando uma função
# Creating a sum function that returns arg1 + arg2
def soma(arg1=0,arg2=0):
    ''' This function returns the sum of arg1 and arg2'''
    return arg1+arg2 # Output a+b

x = soma(5,8) # Calling a function and putting it inside the variable
print(x) 

# Creating a function that returns a factorial of a number
def factorial(arg1):
    x = 1 # It must start from 1
    for i in range(1,arg1+1):
        x *= i # Factorial of a number
    return x # returning the factorial of a number
fac_of_number = factorial(5)
print(fac_of_number)