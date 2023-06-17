'''
Iterate both lists simultaneously
Given a two Python list. 
Write a program to iterate both lists simultaneously and display items from list1 in 
original order and items from list2 in reverse order.
'''
import random as rd

while True:
    list1, list2 =[],[] # Initializing every list

    # Populating each list
    for i in range(1,6):
        list1.append(rd.randrange(20,100))
        list2.append(rd.randrange(20,100))
    print(list1,list2)
    list2.reverse() # Reversing the list2
    for j in range(0,6):
        print(list1[j],list2[j]) # Showing each list1 and list2 element
    break