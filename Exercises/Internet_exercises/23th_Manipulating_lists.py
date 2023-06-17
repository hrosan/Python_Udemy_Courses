'''
Faça uma lista de compras
O usuario deve ter a possibilidade de: INSERIR, APAGAR E LISTAR VALORES
Não permita que o programa quebre com erros de indices inexistentes na lista
'''
import os
# ------------------------------------------------------------------------
lista_items = ["Arroz",'Café','Feijão','Chocolate'] # Itens that people can buy
valor_itens = [8.99, 5.65, 3.25, 1.33] # Item's value
# ------------------------------------------------------------------------
lista_compras = [] # Initialized here because we need to Remove/Add itens inside the infinite loop
user_input = ""
while True:
    os.system('cls') # Clear the prompt
    itens_compra = ["",0] # This list will be arranged inside the purchase list.
    i,item = 0, "" # Itens index and itens name

    # itens compra has a lenght of 2, 1st iten stands for the iten's name and 2nd stands for iten's price
    
    '''
    1st - Ask for what the user wants -> BUY,SUM or REMOVE
    '''

    user_input = input('What do you wanna do Buy/Sum/Remove: ') # Get the user input
    while user_input.lower() not in ["buy","sum","remove"]: # Trying to get the right input
        user_input = input('What do you wanna do Buy/Sum/Remove: ')
    '''
    2nd - Informating what the user wanna buy
    '''
    if user_input.lower() == "buy":
        # Asking for what the customer want to buy
        user_input = input("Wich item do you wanna buy: ")
        while user_input.capitalize() not in lista_items: # Getting the correct answer
            user_input = input("Wich item do you wanna buy: ")
        # Search the item's index inside the lista_item using for loop
        for i,item in enumerate(lista_items):
            if user_input.lower() == item.lower(): # Getting the correct elemente inside the list
                itens_compra[0] = item
                itens_compra[1] = valor_itens[i]
        lista_compras.append(itens_compra) # Putting the elements
    elif user_input.lower() == "remove":
        flag_answer = 0
        # Firs we need to show what are within the list so
        for i,item in enumerate(lista_compras): # Showing what are in every position of list
            print(i, item) # showing every item inside the list
        flag_answer = int(input("Insert the index you want to remove: "))
        while flag_answer < 0 or flag_answer > len(lista_compras) :
            flag_answer = int(input("Insert the index you want to remove: "))
        if 0 <= flag_answer < len(lista_compras):
            del lista_compras[flag_answer] # removing the item though the index
        for i,item in enumerate(lista_compras):
            print(i,item)
    elif user_input.lower() == "sum":
        purchase_sum = 0
        if lista_compras == "":
            break
        else:
            for i in lista_compras: # Taking every item within lista_compras
                purchase_sum += i[1] # Sum every value inside linked with the itens 
            print(f'The total value is R${purchase_sum:.2f}')    
    
