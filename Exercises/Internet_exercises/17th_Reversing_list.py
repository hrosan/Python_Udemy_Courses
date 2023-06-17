'''
Reverse a list in Python
'''
import random as rd

while True:
    random_list = [] # List to get the number

    for i in range(1,8):
        random_list.append(rd.randrange(10,200))
    print(random_list)
    random_list.reverse() # Reverse the list
    print(random_list)
    break