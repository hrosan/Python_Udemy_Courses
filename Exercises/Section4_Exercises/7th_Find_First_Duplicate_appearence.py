'''
    Crie uma função que encontra o primeiro duplicado considerando o segundo numero como a
duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda ocorrencia do número,
ou seja, o numero duplicado em si.
    Exemplo:
        [1,2,3,->3<-,2,1] > 1,2 e 3 são duplicados, retorne (3)
        [1,2,3,4,5,6] > Retorne -1 (Não tem duplicados)
'''

import random, time

# Generating a list of numbers
list_of_numbers = [random.randint(0,9) for _ in range(10)]
print(list_of_numbers) # List of numbers generated

# Turning the list into a set of numbers
acc = 0 # accumulator
number_set = set(list_of_numbers) # Create a set with the list
print(number_set)

# Casting the number_set into a list of list
set_list = [[item,acc] for item in number_set]
#print(set_list)
flag = False
# Iterating over the list to count total times numbers appear within the list
for itens in list_of_numbers:
    for j in range(len(set_list)):
        if set_list[j][0] == itens: # Verifying if the number is equal from the current list's position
            set_list[j][1] += 1 # Adding +1 in the set_list counter
        if set_list[j][1] == 2:
            print(f'The {set_list[j][0]} number reach the 2nd value')
            flag = True # Flag to don't iterate again
            time.sleep(5)
    if flag == True:
        print('Iteration over!!')
        break

# It can be done in another Way - Make it again

