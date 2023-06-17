'''
Create a new list from a two list using the following condition
Given a two list of numbers, write a program to create a new list such that the new list
should contain odd numbers from the first list and even numbers from the second list.
'''
# Infinite loop
while True:
    # Initializing the variables
    first_list = []
    second_list = []
    list_lenght = 0
    mixed_list = [] # List to mix the elements of the two lists
    # Fulfulling the list with numbers
    list_lenght = input("Input the list's lenght: ")
    while list_lenght.isnumeric() == False: # Removing possible errors with type
        list_lenght = input("Input the list's lenght: ")
    list_lenght = int(list_lenght) # Casting string type into number
    # Fulfilling the first list
    for i in range(list_lenght):
        # Adding the elements inside the list
        first_list.append(int(input(f'Inform the {i+1} element of the 1st list: ')))
    for j in range(list_lenght):
        second_list.append(int(input(f'Inform the {j+1} element of the 2nd list: ')))
    # Mixing up the elements from each list
    for i in first_list: # For each element inside the list 1
        # Verifying if the element is odd
        if i%2 != 0: # If the rest os division is different from 0
            mixed_list.append(i) # adding the odd number into the mixed list
    for i in second_list:
        if i%2 == 0:
            mixed_list.append(i) # adding the even numbers into the mixed list
    print(first_list,"\n",second_list,"\n",mixed_list)