numero = input('Write a number: ')

check_numero = numero.isalpha() # It returns True if the string is numeric, and false if is not

if check_numero == True: # If the value typed is alphabetic goes by here
    print('Wrong choice it is not a number')
else: # If the value typed is a number, it goes by here
    even_odd_check = int(numero)%2 # Making the calculus to get the rest of division
    if even_odd_check == 0: # if the variable is 0, it goes by here
        print(f'{numero} is an even number')
    else: # If the variable is different from 0, it goes by here
        print(f'{numero} is an odd number')