'''
Use a loop to display elements from a given list present at odd index positions
'''
import random as rd

while True:
    variable_list = [] # List toreceive the numbers
    variable_number = 0 # Variable to input numbers into the list
    number_elements = 0 # Number of elements inside the list 

    # Fulfilling the variables
    number_elements = int(input('Enter the number of elements: '))
    for i in range(number_elements+1):
        variable_list.append(rd.randrange(1,100))
    print(variable_list)
    # Showing the odd elements inside the list
    for j in range(number_elements+1):
        if j%2==0:
            continue
        else:
            print(variable_list[j])
    break