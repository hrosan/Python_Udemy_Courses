# USER ENTRY
name = input("Type your name: ")
name_lenght = len(name)

# Validating data
check_name = name.isalpha()
if check_name == False:
    print('Your name contains numeric characters')
else:
    # If cases
    if name_lenght <= 4:
        print(f'The name {name} is short')
    elif 5 <= name_lenght <= 6:
        print(f'The name {name} has a normal lenght')
    else:
        print(f'Your name is big')