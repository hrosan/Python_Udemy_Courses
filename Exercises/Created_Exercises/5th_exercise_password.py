'''   
Write a program that asks to the user a password, 
and if the password won't match with the correct password 'python123', ask again and so on.
Just quit the program if the password is correct
'''

# Askinf for the password
password = input('Enter the password: ')
# Checking the password
check_password = password == 'python123'

# while-loop
while check_password == False: # During the error, it continue here
    print('WRONG PASSWORD!!')
    password = input('Enter you password again: ')
    check_password = password == 'python123' # Check the password
print('Access granted!!')