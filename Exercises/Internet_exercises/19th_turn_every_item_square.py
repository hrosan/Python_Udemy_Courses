'''
Turn every item of a list into its square
Given a list of numbers. write a program to turn every item of a list into its square.
'''
import random as rd

while True:
    random_list = [] # List to input the numbers
    elements_number = 0 # number of elements inside the list

    # Fulfilling the list
    elements_number = rd.randrange(1,10) # List size [2;20]

    # Loop to fulfill the list
    for i in range(elements_number+1):
        random_list.append(rd.randint(2,30))
    print(random_list)

    # Power each list's element
    for i in range(elements_number+1):
        random_list[i] = random_list[i]**2 # Powering the element to square
    print(random_list) 
    break
