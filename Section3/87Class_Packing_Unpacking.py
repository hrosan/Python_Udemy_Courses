'''
Packing and Unpacking
'''

names = ['Henrique', 'Claudia', 'Mariana']
nome1,nome2,nome3 = names #Unpacking the names, it must have the same variables quantity
# that has within the list

print(nome1, nome2, nome3)

# Trying to get less than the total names inside the list
'''
nome1, nome2 = names # There will be an error, because the list has more than 2 items
print(nome1, nome2)
'''

# To obtain the remaining items in the list and store them, a pointer is necessary.
nome1, *remaining = names # The asterisk represents a pointer
print(remaining) # ['Claudia', 'Mariana']