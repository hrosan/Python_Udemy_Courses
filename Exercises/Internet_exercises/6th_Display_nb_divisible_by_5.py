'''
Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5
'''
from random import randint

# Infinite-loop
while True:
    acc = ""
    user_list = [] # Initialize a list
    list_size = int(input('Type the number of elements inside the list: ')) # Insert size of list

    # Fulfilling the list
    for i in range(list_size):
        user_list.append(randint(0,100)) # randint(a,b) generate a random number for the list
    print(user_list)

    # Verifying if the number is 5 multiple
    for i in user_list: # For each element inside the list
        element_checking = i%5 # Getting the rest of division
        if element_checking != 0:
            continue
        else:
            acc += str(i) + "-"
    print(acc)            