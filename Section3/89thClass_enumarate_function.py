'''
enumerate() > enumera iteraveis (indices)
enumerate(list) > create a tuple with 2 args (index, value)
'''

lista1 = ['Henrique', 'Rosan', 'pão', 'cachorro','galo']
lista1.append("Rato")

'''
print(lista_enumerada) # Not readable output
print(next(lista_enumerada)) # It shows the next value inside the list returning a tuple
'''
# USING A FOR-LOOP WITH ENUMERATE
''' ---------------------------------------------------------------
for i in lista_enumerada:
    print(i) # Showing the enumerate list

When the loop is finished, the iterator points to the end of the list and if it try to
iterate over the list again the unreadable output appears again
--------------------------------------------------------------------'''

""" If you want to iterate every time over the list you must use
for i in enumerate(lista1):
    print(i)
"""

'''Unpacking the values from a list using enumerate'''
for i,nome in enumerate(lista1): # For with 2 variables to unpack a enumerate list
    print(i, nome) # Showing the unpacking values from a enumerated list