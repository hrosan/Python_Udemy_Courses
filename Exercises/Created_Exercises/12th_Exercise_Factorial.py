'''
Factorial of a number
'''

while True: # Infinite loop
    # User input
    user_input = int(input("Type a number: "))
    factorial = 1 # It has to start with 1, because 0*[any number] = 0
    i = user_input # Iterator get the user input
    # While loop to calculate the factorial number
    while i > 1: # While i higher than 0 -> it came from the user input to 0 [excluding 0]
        factorial *= i # Accumulator for i iterator
        i -= 1 # decrementing an iterator
    # Showing the result
    print(f'The result of {user_input}! is {factorial}')
    