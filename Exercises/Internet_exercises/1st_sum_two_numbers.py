'''Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers return their product only if the product is equal to or lower
than 1000, else return their sum.'''

while True:
    number1 = int(input('Type a number: ')) # Receiving an entry from the user
    number2 = int(input('Type a second number: ')) # Receiving an entru from the user
    # DON'T FORGET INPUT() FUNCTION GIVES AN STRING AS RETURN
    product = number1 * number2 # SUM number1 and number2
    if product < 1000: # CONDITIONAL FOR NUMBERS_SUM LOWER THAN 1000
        print(f'{number1}x{number2}') # PRINTING THE CALCULUS
        print(f'The result is {product}') # SHOWING THE RESULT
    else: # IF SUM IS EQUAL OR HIGHER THAN 1000
        sum_numbers = number1+number2
        print(f'{number1}+{number2}') # PRINTING THE CALCULUS
        print(f'The result is {sum_numbers}') # SHOWING THE RESULT
        continue #REPEAT