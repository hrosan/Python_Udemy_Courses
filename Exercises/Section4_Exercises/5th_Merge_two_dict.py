'''
Merge two Python dictionaries into one
'''
from os import system
import time
# Create a function to create an dictionary
def dictionary(list1=[],list2=[]): # Named parameters, wait for 2 lists
    """
    - list1 = [] -> list of key to the dictionary
    - list2 = [] -> list of values to the dict
    """
    created_dict = {}
    for i in range(0,len(list1)):
        created_dict[list1[i]] = list2[i] # Creating a dictionary
    return created_dict

dict1 = {} # Initializing the dicts
dict2 = {} # Initializing the dict2
flag = 0 # Flag for some situations
# Giving parameters to the dict
while True:
    system('cls')
    # Starting by creating the variables
    key, value = "", None # Initializing variables for Keys and values
    password = input('What do you wanna do\
    [C]reate a dictionary\
    [U]pdate a dictionary\
                    [E]xit\
                    Waiting >>> ')
    
    if password == ('c' or 'C'):
        
        list_key, list_value = [], [] # Initializing list for keys and values
        elements = int(input('How many elements do you want: '))

        for i in range(0,elements):
            list_key.append(input('Insert your key: '))
            list_value.append(input('Inser the value to the actual key: '))
        print(f'Your keys:{list_key}\nYour values:{list_value}')

        # Fullfiling the dictionaries without asking for the user
        if dict1 == {} and flag == 0:
            dict1 = dictionary(list_key,list_value)
            flag += 1
            time.sleep(2)
            continue
        elif dict1 != {} and flag == 1:
            dict2 = dictionary(list_key,list_value)
            flag += 1
            time.sleep(2)
            continue
        elif (dict1 and dict2) != {} and flag == 2:
            print('Dicts are full, please update the main dict')
        time.sleep(1) # Put it to sleep for 5 seconds

    elif password == ('u' or 'U'):
        if (dict1 or dict2) != {}:
            # Asking for the update type
            update_type = input("Which kind of update do you want to do\
                [V]alue's update\
                [R]emove an information\
                [M]erge information\
                Waiting >>> ")
            if update_type in ['m','M']:
                dict1.update(dict2) #Merging the dictionaries
                dict2.clear() # Clear the dict2
                print(dict1)
                flag = 1 # Starting the flag to 1 to not update dictionary 1
            elif update_type in ['V','v']:
                update_key = ""
                print('Which key do you want update: ')
                for key,value in dict1.items(): # items() methods return a tuple
                    print(f'{key}:{value}')
                update_key = input('Which key do you want update: ')
                if update_key in dict1:
                    dict1[update_key] = input('Insert the new value:')
                else:
                    continue
            elif update_type in ['r','R']:
                update_key = input('Which key do you want to remove: ')
                if update_key in dict1:
                    del dict1[update_key]
        else:
            print('Blank informations, please insert some ....')
            time.sleep(2)
            continue
    elif password == ('e' or 'E'):
        break