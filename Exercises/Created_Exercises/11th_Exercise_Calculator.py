'''
Calculator with while-loop
Making an calculator using while_loop

'''
while True: # Loop Infinito
    # USER ENTRY
    number_1 = float(input('Insert the first number: '))
    number_2 = float(input('Insert the second number: '))
    # Type of calc
    print("Type the operation you wanna do")
    print('"+" for addition / "-" for subtraction / "*" for multiplication / "/" for division / "**" for power')
    operation_symbol = input("Type here your math operation: ")
    # MATH SYMBOL WRONG
    while operation_symbol not in "+-**/":
        print('USER ENTRY WRONG!!')
        operation_symbol = input("Type here your math operation: ")
    # IF CASES
    if operation_symbol == "+":
       calc = number_1 + number_2
       print(f'Your calc {number_1} + {number_2} = {calc:.2f}')
    elif operation_symbol == "-":
        calc = number_1 - number_2
        print(f'Your calc {number_1} - {number_2} = {calc:.2f}')
    elif operation_symbol == "*":
        calc = number_1 * number_2
        print(f'Your calc {number_1} * {number_2} = {calc:.2f}')
    elif operation_symbol == "/":
        try:
            calc = number_1 / number_2
            print(f'Your calc {number_1} / {number_2} = {calc:.2f}')
        except ZeroDivisionError:
            print("DIVISION BY ZERO TRY AGAIN")
            continue
    elif operation_symbol == "**":
        calc = number_1**number_2
        print(f'Your calc {number_1}^{number_2}={calc:.2f}')