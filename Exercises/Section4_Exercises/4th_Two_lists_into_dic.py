'''
Write a Python program to convert them into a dictionary in a way that item from list1 is 
the key and item from list2 is the value
'''
def list_to_dict(list1 = [],list2 = []): #Those entry must be lists
    # Getting the lenght of each list
    len_list1 , len_list2 = len(list1), len(list2) #Getting the dictionary info
    dictionary = {} # Initializing the dictionary
    if len_list1 > len_list2 or len_list2 > len_list1:
        raise IndexError #Raising an error about index
    try:
        for i in range(0,len_list1): 
            dictionary[list1[i]] = list2[i] # Fulfilling the dictionary
    except IndexError:
        return print('Index Error') 
    return dictionary

while True:
    list1 = [] # Lists with the key
    list2 = [] # List with the values

    # The list must have 3 itens within, range will be 3
    for i in range(0,3):
        list1.append(input('Type the key: '))
        list2.append(input('Type the value for the actual key: '))
    print(list1, list2)
    dict_generated = list_to_dict(list1,list2) # Calling a function
    print(dict_generated)
    break
