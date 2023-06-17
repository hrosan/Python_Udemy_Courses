'''
Write a Python program that prompts the user to enter a positive integer,
and then determines if the integer is prime or not. 
A prime number is a number that is only divisible by 1 and itself. If the number is prime, 
the program should print a message saying so. If the number is not prime, 
the program should print a message saying how the number is divisible.
'''
check_number = int(input('Informe um numero: ')) #Asking for a number

first_check = check_number%1 # Getting the rest of a division
if(first_check==0):
    print(f'{check_number} é divisivel por 1')

second_check = check_number%check_number
if(second_check == 0):
    print(f'O numero {check_number} é divisilvel por si mesmo')