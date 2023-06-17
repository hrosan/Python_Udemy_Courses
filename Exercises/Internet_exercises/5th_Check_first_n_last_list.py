'''
Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. 
If numbers are different then return False.
'''

# Infinite-loop
while True:
    nb_list = [] # List to keep the numbers
    # Fulfilling the list with numbers
    nb_list_iterator = input('How many number do you want to put inside the list: ')
    # Checking if the input is a number of not
    while nb_list_iterator.isnumeric() == False:
        # While is not a number, keep asking for a number
        nb_list_iterator = int(input('How many number do you want to put inside the list: '))
    # Iterating with the list
    for i in range(int(nb_list_iterator)):
        nb_list.append(int(input('Type a number: '))) # Fulfilling the list
    print(nb_list)
    # Comparing the first and the last items inside the list
    if nb_list[0] != nb_list[nb_list_iterator-1]:
        print("False")
    else:
        print('True')
