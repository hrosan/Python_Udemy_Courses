'''
Concatenate two lists index-wise
Write a program to add two lists index-wise. 
Create a new list that contains the 0th index item from both the list, 
then the 1st index item, and so on till the last element. 
Any leftover items will get added at the end of the new list.
'''

# Variable
lista_1 = ["M","na","i","Hen"]
lista_2 = ["y","me",'s',"rique"]
lista_3 = []

for i in range(len(lista_1)):
    lista_3.append(lista_1[i] + lista_2[i]) # Concatenating the elements of each list
print(lista_3)